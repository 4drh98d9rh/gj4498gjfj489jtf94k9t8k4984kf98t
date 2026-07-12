import asyncio
import json
import os
import hashlib
import secrets
import time
import aiofiles
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote, parse_qs
from collections import deque, defaultdict
from pathlib import Path

import psutil
from typing import Optional
from fastapi import FastAPI, Request, HTTPException, WebSocket, WebSocketDisconnect, Depends, Query
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx
import logging
import re

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("MX-UI")

IRAN_TZ = ZoneInfo("Asia/Tehran")

app = FastAPI(title="MX-UI", docs_url=None, redoc_url=None)

# ── Persistence ───────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "mxui_state.json"
SECRET_FILE = DATA_DIR / "mxui_secret.key"
SAVE_LOCK = asyncio.Lock()

def _load_or_create_secret() -> str:
    env_secret = os.environ.get("SECRET_KEY")
    if env_secret:
        return env_secret
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SECRET_FILE.exists():
            existing = SECRET_FILE.read_text(encoding="utf-8").strip()
            if existing:
                return existing
        new_secret = secrets.token_urlsafe(32)
        SECRET_FILE.write_text(new_secret, encoding="utf-8")
        return new_secret
    except Exception as e:
        logger.warning(f"Could not persist SECRET_KEY: {e}")
        return secrets.token_urlsafe(32)

CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": _load_or_create_secret(),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
    "dashboard_path": "/dashboard",
    "login_path": "/login",
    "sub_path": "/sub",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def load_state():
    global LINKS, AUTH, CONFIG
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                raw = await f.read()
            data = json.loads(raw)
            LINKS.update(data.get("links", {}))
            if "password_hash" in data:
                AUTH["password_hash"] = data["password_hash"]
            if "paths" in data:
                for key, value in data["paths"].items():
                    CONFIG[key] = value
            logger.info(f"State loaded: {len(LINKS)} links")
    except Exception as e:
        logger.warning(f"Could not load state: {e}")

async def save_state():
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            data = {
                "links": dict(LINKS),
                "password_hash": AUTH["password_hash"],
                "saved_at": datetime.now().isoformat(),
                "paths": {
                    "dashboard_path": CONFIG.get("dashboard_path", "/dashboard"),
                    "login_path": CONFIG.get("login_path", "/login"),
                    "sub_path": CONFIG.get("sub_path", "/sub"),
                }
            }
            tmp = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")

# ── In-memory state ───────────────────────────────────────────────────────────
connections: dict = {}
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs: deque = deque(maxlen=50)
activity_logs: deque = deque(maxlen=200)
hourly_traffic: dict = defaultdict(int)
http_client: httpx.AsyncClient | None = None
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()

PROTOCOLS = ("vless-ws", "xhttp-packet-up", "xhttp-stream-up")
DEFAULT_PROTOCOL = "vless-ws"
FINGERPRINTS = ("chrome", "firefox", "safari", "ios", "android", "edge", "360", "qq", "random", "randomized")
DEFAULT_FINGERPRINT = "chrome"
DEFAULT_ALPN_BY_PROTOCOL = {
    "vless-ws": "http/1.1",
    "xhttp-packet-up": "h2,http/1.1",
    "xhttp-stream-up": "h2,http/1.1",
}
DEFAULT_PORT = 443  # fixed, not changeable
DEFAULT_SPEED_LIMIT = 0

def log_activity(kind: str, message: str, level: str = "info"):
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })

# ── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "mxui_session"
SESSION_TTL = 60 * 60 * 24 * 365

def hash_password(pw: str) -> str:
    return hashlib.sha256(f"{pw}{CONFIG['secret']}".encode()).hexdigest()

AUTH = {"password_hash": hash_password(os.environ.get("ADMIN_PASSWORD", "MUVIXO"))}
SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token

async def is_valid_session(token: str | None) -> bool:
    if not token:
        return False
    async with SESSIONS_LOCK:
        exp = SESSIONS.get(token)
        if exp is None:
            return False
        if exp < time.time():
            SESSIONS.pop(token, None)
            return False
        return True

async def destroy_session(token: str | None):
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)

async def require_auth(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(status_code=401, detail="unauthorized")
    return token

# ── Startup / Shutdown ────────────────────────────────────────────────────────
@app.on_event("startup")
async def startup():
    global http_client
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(
        limits=limits, timeout=timeout, follow_redirects=True,
    )
    await load_state()
    log_activity("system", "Server started", "ok")
    logger.info(f"MX-UI v1.0.0 started on port {CONFIG['port']}")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    if http_client:
        await http_client.aclose()

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_host(request: Optional[Request] = None) -> str:
    if request is not None:
        h = request.headers.get("x-forwarded-host") or request.headers.get("host")
        if h:
            h = h.split(":")[0]
            CONFIG["host"] = h
            return h
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", CONFIG["host"])

def generate_uuid() -> str:
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)

def generate_vless_link(
    uuid: str,
    host: str,
    remark: str = "MX-UI",
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str | None = None,
    alpn: str | None = None,
) -> str:
    fp = (fingerprint or DEFAULT_FINGERPRINT).strip() or DEFAULT_FINGERPRINT
    if fp not in FINGERPRINTS:
        fp = DEFAULT_FINGERPRINT
    alpn_val = (alpn or "").strip() or DEFAULT_ALPN_BY_PROTOCOL.get(protocol, "http/1.1")
    port_val = DEFAULT_PORT  # fixed

    if protocol == "vless-ws":
        path = f"/ws/{uuid}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "ws",
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    else:
        mode = protocol.replace("xhttp-", "")
        path = f"/xhttp-siz10/{mode}/{uuid}"
        params = {
            "encryption": "none",
            "security": "tls",
            "type": "xhttp",
            "mode": mode,
            "host": host,
            "path": path,
            "sni": host,
            "fp": fp,
            "alpn": alpn_val,
        }
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"vless://{uuid}@{host}:{port_val}?{query}#{quote(remark)}"

def vless_link_for_link(link: dict, uid: str, host: str) -> str:
    proto = link.get("protocol", DEFAULT_PROTOCOL)
    return generate_vless_link(
        uid, host,
        remark=f"MX-UI-{link.get('label','')}",
        protocol=proto,
        fingerprint=link.get("fingerprint"),
        alpn=link.get("alpn"),
    )

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB": return int(value * 1024 ** 3)
    if unit == "MB": return int(value * 1024 ** 2)
    if unit == "KB": return int(value * 1024)
    return int(value)

def parse_speed_to_bytes(value: float, unit: str) -> int:
    if value <= 0:
        return 0
    unit = (unit or "MBIT").upper()
    if unit == "MBIT":
        return int(value * 1024 * 1024 / 8)
    if unit == "KB":
        return int(value * 1024)
    if unit == "MB":
        return int(value * 1024 * 1024)
    return int(value)

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def fmt_bytes(b: int) -> str:
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.1f} KB"
    if b < 1024**3: return f"{b/1024**2:.2f} MB"
    return f"{b/1024**3:.2f} GB"

def fmt_bytes_short(b: int) -> str:
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.0f} KB"
    if b < 1024**3: return f"{b/1024**2:.0f} MB"
    return f"{b/1024**3:.2f} GB"

def unique_ips_for_uuid(uuid: str) -> set:
    return {c.get("ip") for c in connections.values() if c.get("uuid") == uuid and c.get("ip")}

def is_ip_allowed(link: dict | None, uuid: str, ip: str) -> bool:
    if link is None:
        return False
    limit = int(link.get("ip_limit", 0) or 0)
    if limit <= 0:
        return True
    ips = unique_ips_for_uuid(uuid)
    if ip in ips:
        return True
    return len(ips) < limit

def client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "unknown"

# ── Default link ──────────────────────────────────────────────────────────────
_default_link_created = False

async def ensure_default_link():
    global _default_link_created
    if _default_link_created:
        return
    async with LINKS_LOCK:
        if not any(l.get("is_default") for l in LINKS.values()):
            uid = hashlib.sha256(f"default{CONFIG['secret']}".encode()).hexdigest()
            uid = f"{uid[:8]}-{uid[8:12]}-{uid[12:16]}-{uid[16:20]}-{uid[20:32]}"
            if uid not in LINKS:
                LINKS[uid] = {
                    "label": "Default Link",
                    "limit_bytes": 0,
                    "used_bytes": 0,
                    "created_at": datetime.now().isoformat(),
                    "active": True,
                    "expires_at": None,
                    "note": "",
                    "is_default": True,
                    "protocol": DEFAULT_PROTOCOL,
                    "fingerprint": DEFAULT_FINGERPRINT,
                    "alpn": "",
                    "ip_limit": 0,
                    "speed_limit_bytes": DEFAULT_SPEED_LIMIT,
                    "last_used": None,
                }
                asyncio.create_task(save_state())
        _default_link_created = True

# ── Basic endpoints ───────────────────────────────────────────────────────────
@app.get("/")
async def root():
    dashboard_path = CONFIG.get("dashboard_path", "/dashboard")
    return RedirectResponse(url=dashboard_path)

@app.get("/health")
async def health():
    return {"status": "ok", "connections": len(connections), "uptime": uptime()}

# ── Subscription endpoints ────────────────────────────────────────────────────

@app.get("/sub/user")
async def subscription_user(request: Request, uuid: str = Query(...)):
    sub_path = CONFIG.get("sub_path", "/sub")
    if not request.url.path.startswith(sub_path):
        return RedirectResponse(url=f"{sub_path}/user?uuid={uuid}")
    
    from pages import SUB_USER_HTML
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link:
        raise HTTPException(status_code=404, detail="not found")
    host = get_host(request)
    vless = vless_link_for_link(link, uuid, host)
    used = link.get("used_bytes", 0)
    limit = link.get("limit_bytes", 0)
    active = is_link_allowed(link)
    expiry = link.get("expires_at", "No expiry")
    last_online = link.get("last_used", "Never")
    ips = unique_ips_for_uuid(uuid)
    ip_display = ", ".join(ips) if ips else "No active connections"
    status_text = "Active" if active else "Inactive"
    status_color = "text-emerald-400" if active else "text-red-400"
    status_html = f'<span class="{status_color} font-semibold">{status_text}</span>'
    quota_str = "∞" if limit == 0 else fmt_bytes(limit)
    remained = "∞" if limit == 0 else fmt_bytes(max(0, limit - used))
    usage_pct = 0 if limit == 0 else min(100, (used / limit) * 100)
    downloaded = fmt_bytes(used)
    uploaded = "0 B"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={quote(vless)}"
    return HTMLResponse(content=SUB_USER_HTML.format(
        uuid=uuid,
        label=link.get("label", "Unknown"),
        vless_link=vless,
        qr_url=qr_url,
        status=status_html,
        downloaded=downloaded,
        uploaded=uploaded,
        usage=fmt_bytes(used),
        total_quota=quota_str,
        remained=remained,
        last_online=last_online,
        expiry=expiry,
        ips=ip_display,
        usage_pct=round(usage_pct, 1),
        used_fmt=fmt_bytes(used),
        limit_fmt=quota_str,
        watermark="Created by Muvixo"
    ))

@app.get("/sub/{uuid}")
async def subscription_single(uuid: str, request: Request):
    sub_path = CONFIG.get("sub_path", "/sub")
    if not request.url.path.startswith(sub_path):
        return RedirectResponse(url=f"{sub_path}/{uuid}")
    
    import base64
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link or not is_link_allowed(link):
        raise HTTPException(status_code=404, detail="not found or inactive")
    host = get_host(request)
    vless = vless_link_for_link(link, uuid, host)
    content = base64.b64encode(vless.encode()).decode()
    return Response(content=content, media_type="text/plain",
                    headers={"profile-title": quote(link["label"]), "support-url": "https://t.me/Farajian2004f"})

@app.get("/sub/{uuid}/info", response_class=HTMLResponse)
async def subscription_info(uuid: str, request: Request):
    sub_path = CONFIG.get("sub_path", "/sub")
    if not request.url.path.startswith(sub_path):
        return RedirectResponse(url=f"{sub_path}/{uuid}/info")
    
    from pages import SUB_INFO_HTML
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not link:
        raise HTTPException(status_code=404, detail="not found")
    host = get_host(request)
    return HTMLResponse(content=SUB_INFO_HTML.format(
        uuid=uuid,
        label=link.get("label", "Unknown"),
        used_fmt=fmt_bytes(link.get("used_bytes", 0)),
        limit_fmt="∞" if link.get("limit_bytes", 0) == 0 else fmt_bytes(link["limit_bytes"]),
        expires_at=link.get("expires_at", "No expiry"),
        active=link.get("active", True),
        vless_link=vless_link_for_link(link, uuid, host),
        sub_url=f"https://{host}/sub/{uuid}",
        watermark="Created by Muvixo"
    ))

# ── Subscription all (requires auth) ──────────────────────────────────────
@app.get("/sub-all")
async def subscription_all(request: Request, _=Depends(require_auth)):
    sub_path = CONFIG.get("sub_path", "/sub")
    if not request.url.path.startswith(sub_path + "-all"):
        return RedirectResponse(url=f"{sub_path}-all")
    
    import base64
    host = get_host(request)
    async with LINKS_LOCK:
        lines = [
            vless_link_for_link(d, uid, host)
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")

# ── Auth endpoints ────────────────────────────────────────────────────────────
@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)
    if hash_password(str(body.get("password", ""))) != AUTH["password_hash"]:
        log_activity("auth", f"Failed login from {ip}", "err")
        raise HTTPException(status_code=401, detail="Wrong password")
    token = await create_session()
    log_activity("auth", f"Successful login from {ip}", "ok")
    
    secure = False
    resp = JSONResponse({"ok": True})
    resp.set_cookie(
        SESSION_COOKIE,
        token,
        max_age=SESSION_TTL,
        httponly=True,
        samesite="lax",
        path="/",
        secure=secure,
    )
    logger.info(f"Login cookie set: secure={secure}, token={token[:8]}...")
    return resp

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    secure = request.url.scheme == "https"
    resp.delete_cookie(SESSION_COOKIE, path="/", secure=secure)
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

@app.post("/api/change-password")
async def api_change_password(request: Request, token=Depends(require_auth)):
    body = await request.json()
    if hash_password(str(body.get("current_password", ""))) != AUTH["password_hash"]:
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    new = str(body.get("new_password", ""))
    if len(new) < 4:
        raise HTTPException(status_code=400, detail="New password must be at least 4 characters")
    AUTH["password_hash"] = hash_password(new)
    async with SESSIONS_LOCK:
        SESSIONS.clear()
        SESSIONS[token] = time.time() + SESSION_TTL
    await save_state()
    log_activity("auth", "Panel password changed", "ok")
    return {"ok": True}

# ── Settings endpoints ────────────────────────────────────────────────────────
@app.get("/api/get-paths")
async def get_paths(_=Depends(require_auth)):
    return {
        "dashboard_path": CONFIG.get("dashboard_path", "/dashboard"),
        "login_path": CONFIG.get("login_path", "/login"),
        "sub_path": CONFIG.get("sub_path", "/sub"),
    }

@app.post("/api/update-path")
async def update_path(request: Request, _=Depends(require_auth)):
    body = await request.json()
    path_type = body.get("path_type")
    new_path = body.get("new_path", "").strip()
    
    if not path_type or path_type not in ["dashboard", "login", "sub"]:
        raise HTTPException(status_code=400, detail="Invalid path type")
    
    if not new_path or not new_path.startswith("/"):
        raise HTTPException(status_code=400, detail="Path must start with /")
    
    if not re.match(r'^/[a-zA-Z0-9\-_/]*$', new_path):
        raise HTTPException(status_code=400, detail="Path contains invalid characters")
    
    CONFIG[f"{path_type}_path"] = new_path
    await save_state()
    log_activity("settings", f"{path_type} path changed to {new_path}", "ok")
    return {"ok": True, "path": new_path}

@app.get("/api/is-default-password")
async def is_default_password():
    default_hash = hash_password("MUVIXO")
    return {"is_default": AUTH["password_hash"] == default_hash}

@app.get("/api/current-paths")
async def get_current_paths():
    return {
        "dashboard": CONFIG.get("dashboard_path", "/dashboard"),
        "login": CONFIG.get("login_path", "/login"),
        "sub": CONFIG.get("sub_path", "/sub"),
    }

# ── Stats ─────────────────────────────────────────────────────────────────────
@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_count = psutil.cpu_count(logical=True)
    ram = psutil.virtual_memory()
    swap = psutil.swap_memory()
    disk = psutil.disk_usage('/')
    total_links = len(snap)
    active_links = sum(1 for l in snap.values() if is_link_allowed(l))
    total_traffic_mb = round(stats["total_bytes"] / (1024 ** 2), 2)

    return {
        "active_connections": len(connections),
        "total_traffic_mb": total_traffic_mb,
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "uptime": uptime(),
        "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic),
        "recent_errors": list(error_logs)[-10:],
        "links_count": total_links,
        "active_links": active_links,
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
        "cpu_percent": round(cpu_percent, 1),
        "cpu_cores": cpu_count,
        "ram_used_mb": ram.used // (1024 * 1024),
        "ram_total_mb": ram.total // (1024 * 1024),
        "ram_percent": ram.percent,
        "swap_used_mb": swap.used // (1024 * 1024),
        "swap_total_mb": swap.total // (1024 * 1024),
        "swap_percent": swap.percent,
        "disk_used_gb": round(disk.used / (1024**3), 2),
        "disk_total_gb": round(disk.total / (1024**3), 2),
        "disk_percent": disk.percent,
    }

@app.get("/api/activity")
async def get_activity(_=Depends(require_auth)):
    return {"logs": list(activity_logs)[-150:]}

@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    grouped: dict[str, dict] = {}
    async with LINKS_LOCK:
        snap = dict(LINKS)
    for conn_id, c in connections.items():
        ip = c.get("ip", "unknown")
        link = snap.get(c.get("uuid"))
        label = link.get("label") if link else "unknown"
        g = grouped.get(ip)
        if g is None:
            g = {
                "ip": ip,
                "sessions": 0,
                "bytes": 0,
                "labels": set(),
                "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            grouped[ip] = g
        g["sessions"] += 1
        g["bytes"] += c.get("bytes", 0)
        g["labels"].add(label)
        g["transports"].add(c.get("transport", "vless-ws"))
        ca = c.get("connected_at")
        if ca:
            if not g["first_connected_at"] or ca < g["first_connected_at"]:
                g["first_connected_at"] = ca
            if not g["last_connected_at"] or ca > g["last_connected_at"]:
                g["last_connected_at"] = ca
    result = []
    for ip, g in grouped.items():
        result.append({
            "ip": ip,
            "sessions": g["sessions"],
            "labels": sorted(g["labels"]),
            "label": " · ".join(sorted(g["labels"])) if g["labels"] else "unknown",
            "transports": sorted(g["transports"]),
            "bytes": g["bytes"],
            "bytes_fmt": fmt_bytes(g["bytes"]),
            "connected_at": g["first_connected_at"],
            "last_connected_at": g["last_connected_at"],
        })
    result.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)
    return {
        "connections": result,
        "count": len(result),
        "raw_count": len(connections),
    }

# ── Link Management ───────────────────────────────────────────────────────────
async def make_link(
    label: str = "New Link",
    limit_bytes: int = 0,
    expires_at: str | None = None,
    note: str = "",
    protocol: str = DEFAULT_PROTOCOL,
    fingerprint: str = DEFAULT_FINGERPRINT,
    alpn: str = "",
    ip_limit: int = 0,
    speed_limit_bytes: int = 0,
) -> tuple[str, dict]:
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    fingerprint = (fingerprint or DEFAULT_FINGERPRINT).strip().lower()
    if fingerprint not in FINGERPRINTS:
        fingerprint = DEFAULT_FINGERPRINT
    uid = generate_uuid()
    async with LINKS_LOCK:
        LINKS[uid] = {
            "label": (label or "New Link").strip()[:60] or "New Link",
            "limit_bytes": max(0, limit_bytes),
            "used_bytes": 0,
            "created_at": datetime.now().isoformat(),
            "active": True,
            "expires_at": expires_at,
            "note": (note or "").strip()[:200],
            "is_default": False,
            "protocol": protocol,
            "fingerprint": fingerprint,
            "alpn": (alpn or "").strip()[:100],
            "ip_limit": max(0, ip_limit),
            "speed_limit_bytes": max(0, speed_limit_bytes),
            "last_used": None,
        }
    asyncio.create_task(save_state())
    log_activity("link", f"Config «{LINKS[uid]['label']}» created", "ok")
    return uid, LINKS[uid]

async def remove_link(uid: str) -> str | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        label = LINKS[uid].get("label", uid)
        del LINKS[uid]
    asyncio.create_task(save_state())
    log_activity("link", f"Config «{label}» deleted", "err")
    return label

async def set_link_active(uid: str, active: bool) -> dict | None:
    async with LINKS_LOCK:
        if uid not in LINKS:
            return None
        LINKS[uid]["active"] = bool(active)
        label = LINKS[uid]["label"]
    log_activity("link", f"Config «{label}» {'activated' if active else 'deactivated'}", "ok" if active else "warn")
    asyncio.create_task(save_state())
    return LINKS[uid]

@app.post("/api/links")
async def create_link(request: Request, _=Depends(require_auth)):
    body = await request.json()
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    expires_at = (datetime.now() + timedelta(days=exp_days)).isoformat() if exp_days > 0 else None
    try:
        ip_limit = int(body.get("ip_limit") or 0)
    except (TypeError, ValueError):
        ip_limit = 0

    sv = float(body.get("speed_limit_value") or 0)
    su = body.get("speed_limit_unit") or "MBIT"
    speed_limit_bytes = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)

    uid, link = await make_link(
        label=body.get("label") or "New Link",
        limit_bytes=limit_bytes,
        expires_at=expires_at,
        note=body.get("note") or "",
        protocol=body.get("protocol") or DEFAULT_PROTOCOL,
        fingerprint=body.get("fingerprint") or DEFAULT_FINGERPRINT,
        alpn=body.get("alpn") or "",
        ip_limit=ip_limit,
        speed_limit_bytes=speed_limit_bytes,
    )

    host = get_host(request)
    return {
        "uuid": uid,
        **link,
        "expired": False,
        "vless_link": vless_link_for_link(link, uid, host),
        "sub_url": f"https://{host}/sub/{uid}",
        "info_url": f"https://{host}/sub/{uid}/info",
    }

@app.get("/api/links")
async def list_links(request: Request, _=Depends(require_auth)):
    host = get_host(request)
    async with LINKS_LOCK:
        snap = dict(LINKS)
    result = []
    for uid, d in snap.items():
        proto = d.get("protocol", DEFAULT_PROTOCOL)
        result.append({
            "uuid": uid,
            **d,
            "protocol": proto,
            "expired": is_link_expired(d),
            "vless_link": vless_link_for_link(d, uid, host),
            "sub_url": f"https://{host}/sub/{uid}",
            "info_url": f"https://{host}/sub/{uid}/info",
            "connected_ips": len(unique_ips_for_uuid(uid)),
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        label = link.get("label")
        if "active" in body:
            link["active"] = bool(body["active"])
            log_activity("link", f"Config «{label}» {'activated' if link['active'] else 'deactivated'}", "ok" if link["active"] else "warn")
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
            log_activity("link", f"Usage reset for «{label}»", "info")
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            link["expires_at"] = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
        if "fingerprint" in body:
            fp = str(body.get("fingerprint") or DEFAULT_FINGERPRINT).strip().lower()
            link["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
        if "alpn" in body:
            link["alpn"] = str(body.get("alpn") or "").strip()[:100]
        if "ip_limit" in body:
            try:
                il = int(body.get("ip_limit") or 0)
            except (TypeError, ValueError):
                il = 0
            link["ip_limit"] = max(0, il)
        if "speed_limit_value" in body:
            sv = float(body.get("speed_limit_value") or 0)
            su = body.get("speed_limit_unit") or "MBIT"
            link["speed_limit_bytes"] = 0 if sv <= 0 else parse_speed_to_bytes(sv, su)
            from speed_limit import reset_bucket
            reset_bucket(uid)
        if any(k in body for k in ("label", "note", "limit_value", "expires_days", "fingerprint", "alpn", "ip_limit", "speed_limit_value")):
            log_activity("link", f"Config «{link['label']}» updated", "info")
    asyncio.create_task(save_state())
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, _=Depends(require_auth)):
    label = await remove_link(uid)
    if label is None:
        raise HTTPException(status_code=404, detail="link not found")
    return {"ok": True, "deleted": uid}

# ── VLESS Relay ──────────────────────────────────────────────────────────────
from relay_vless import websocket_tunnel
app.add_api_websocket_route("/ws/{uuid}", websocket_tunnel)

# ── XHTTP ─────────────────────────────────────────────────────────────────────
from xhttp import router as xhttp_router
app.include_router(xhttp_router)

# ── HTTP Proxy ────────────────────────────────────────────────────────────────
_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization",
        "te","trailers","transfer-encoding","upgrade","content-encoding","content-length"}

@app.api_route("/proxy/{target_url:path}", methods=["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"])
async def http_proxy(target_url: str, request: Request):
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    try:
        body = await request.body()
        headers = {k: v for k, v in request.headers.items() if k.lower() not in _HOP and k.lower() != "host"}
        resp = await http_client.request(method=request.method, url=target_url, headers=headers, content=body)
        stats["total_bytes"] += len(resp.content)
        stats["total_requests"] += 1
        hourly_traffic[now_ir().strftime("%H:00")] += len(resp.content)
        return Response(content=resp.content, status_code=resp.status_code,
                        headers={k: v for k, v in resp.headers.items() if k.lower() not in _HOP})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "url": target_url, "time": datetime.now().isoformat()})
        raise HTTPException(status_code=502, detail=f"Proxy error: {exc}")

# ── HTML Pages ─────────────────────────────────────────────────────────────────
from pages import LOGIN_HTML, DASHBOARD_HTML

# Main dashboard handler - handles all dashboard paths
@app.get("/dash")
@app.get("/dashboard")
@app.get(CONFIG.get("dashboard_path", "/dashboard"))
async def dashboard(request: Request):
    dashboard_path = CONFIG.get("dashboard_path", "/dashboard")
    
    # If someone visits /dashboard but we're using /dash, redirect
    if request.url.path == "/dashboard" and dashboard_path != "/dashboard":
        return RedirectResponse(url=dashboard_path)
    
    # If someone visits the current dashboard path
    if request.url.path == dashboard_path:
        token = request.cookies.get(SESSION_COOKIE)
        logger.info(f"Dashboard received cookie: {token}")
        valid = await is_valid_session(token)
        logger.info(f"Dashboard session valid: {valid}")
        if not valid:
            login_path = CONFIG.get("login_path", "/login")
            return RedirectResponse(url=login_path)
        await ensure_default_link()
        return HTMLResponse(content=DASHBOARD_HTML)
    
    # If someone visits some other path that starts with /dash but isn't our path
    if request.url.path.startswith("/dash"):
        return RedirectResponse(url=dashboard_path)
    
    # Fallback - redirect to dashboard
    return RedirectResponse(url=dashboard_path)

# Login page handler
@app.get("/login")
@app.get(CONFIG.get("login_path", "/login"))
async def login_page(request: Request):
    login_path = CONFIG.get("login_path", "/login")
    if request.url.path != login_path and request.url.path != "/login":
        return RedirectResponse(url=login_path)
    
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        dashboard_path = CONFIG.get("dashboard_path", "/dashboard")
        return RedirectResponse(url=dashboard_path)
    
    # Check if default password is used
    is_default = AUTH["password_hash"] == hash_password("MUVIXO")
    login_html = LOGIN_HTML
    
    # If default password is changed, show message
    if not is_default:
        login_html = login_html.replace(
            '<span class="text-xs font-mono font-bold text-blue-400 bg-blue-500/10 px-2 py-1 rounded border border-blue-500/20 cursor-pointer hover:bg-blue-500/20 transition" onclick="document.getElementById(\'pw\').value=\'MUVIXO\';document.getElementById(\'pw\').focus()">MUVIXO</span>',
            '<span class="text-xs font-mono font-bold text-amber-400 bg-amber-500/10 px-2 py-1 rounded border border-amber-500/20">Password changed</span>'
        )
        login_html = login_html.replace(
            '<span class="text-xs text-slate-400">Default password</span>',
            '<span class="text-xs text-slate-400">Default password</span><span class="text-xs text-amber-400 ml-2">(changed)</span>'
        )
    
    return HTMLResponse(content=login_html)

# Sub path handler
@app.get("/sub")
async def sub_path_handler():
    sub_path = CONFIG.get("sub_path", "/sub")
    if sub_path != "/sub":
        return RedirectResponse(url=sub_path)
    return RedirectResponse(url="/sub")

# ── Catch-all route for any unknown path ─────────────────────────────────────
@app.get("/{path:path}")
async def catch_all(request: Request, path: str):
    """Redirect any unknown path to dashboard"""
    # Skip API routes
    if path.startswith("api/") or path.startswith("stats") or path.startswith("health"):
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Skip static files and common paths
    if path.startswith("favicon") or path.startswith("robots") or path.startswith(".well-known"):
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Skip websocket and xhttp paths
    if path.startswith("ws/") or path.startswith("xhttp-siz10/"):
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Skip proxy paths
    if path.startswith("proxy/"):
        raise HTTPException(status_code=404, detail="Not Found")
    
    # Redirect to dashboard
    dashboard_path = CONFIG.get("dashboard_path", "/dashboard")
    return RedirectResponse(url=dashboard_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
