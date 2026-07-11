# MX-UI v1.0.0

Modern VLESS/XHTTP tunnel gateway with a beautiful dashboard, per‑config subscription links with volume, speed, IP limits, and expiry.

## Features

- VLESS over WebSocket and XHTTP (packet‑up, stream‑up)
- HTTP proxy
- Full management dashboard with live stats, hourly traffic charts, active connections, error logs
- Unlimited configs with per‑link traffic, speed, IP limit, expiry, and active/inactive toggle
- QR code for each link and subscription
- Fingerprint (uTLS) and ALPN per config
- Customisable port per config
- Subscription info page per config (shows volume, UUID, usage, expiry)
- Persistent state on disk (requires a persistent volume for `/data`)

## Deploy

1. Fork this repo on GitHub.
2. Deploy on Railway (or any platform that supports Python).
3. Set `ADMIN_PASSWORD=MUVIXO` (or change it) and ensure a persistent volume is mounted at `/data`.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ADMIN_PASSWORD` | Dashboard login password | `MUVIXO` |
| `SECRET_KEY` | Session signing secret (auto‑generated) | – |
| `DATA_DIR` | Persistent state directory | `/data` |
| `RAILWAY_PUBLIC_DOMAIN` | Public domain (set automatically on Railway) | `localhost` |

## Usage

- Dashboard: `https://your‑domain/dashboard`
- Login with password `MUVIXO` (or your custom one)
- Create configs, copy their subscription links, view usage, and manage them via the UI.


---

**Created by Muvixo**