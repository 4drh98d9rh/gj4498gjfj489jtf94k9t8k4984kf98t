# pages.py - MX-UI v1.0.0
# All templates with escaped braces for Python .format()

LOGO_B64 = "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"

# ---------- LOGIN_HTML (escaped braces) ----------
LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login · MX-UI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
    theme: {{
        extend: {{
            fontFamily: {{
                sans: ['Inter', 'sans-serif'],
                mono: ['JetBrains Mono', 'monospace'],
            }}
        }}
    }}
}}
</script>
<style>
body {{ background-color: #070a13; }}
.glow-effect {{ box-shadow: 0 0 25px rgba(59, 130, 246, 0.12); }}
</style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex items-center justify-center bg-[#070a13] relative antialiased tracking-tight p-4">
<div class="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_0%,rgba(59,130,246,0.08),transparent_70%)] pointer-events-none"></div>
<div class="w-full max-w-md relative z-10">
    <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-8 backdrop-blur-xl glow-effect">
        <div class="flex items-center gap-3 mb-6">
            <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
            </div>
            <div>
                <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">MX-UI PANEL</span>
                <span class="text-xs block text-slate-500 font-medium">v1.0.0</span>
            </div>
        </div>
        <h1 class="text-xl font-bold text-slate-100 mb-1">Sign In</h1>
        <p class="text-sm text-slate-400 mb-6">Enter your password to access the dashboard</p>
        <div class="bg-slate-800/40 border border-slate-700/50 rounded-xl p-3 flex items-center justify-between mb-5">
            <span class="text-xs text-slate-400">Default password</span>
            <span class="text-xs font-mono font-bold text-blue-400 bg-blue-500/10 px-2 py-1 rounded border border-blue-500/20 cursor-pointer hover:bg-blue-500/20 transition" onclick="document.getElementById('pw').value='MUVIXO';document.getElementById('pw').focus()">MUVIXO</span>
        </div>
        <form id="loginForm">
            <div class="mb-4">
                <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Password</label>
                <input type="password" id="pw" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition" placeholder="Enter your password" autofocus required>
            </div>
            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 text-white font-medium text-sm px-4 py-2.5 rounded-xl transition duration-200 shadow-lg shadow-blue-600/10 flex items-center justify-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg>
                Sign In
            </button>
            <div id="errorMsg" class="mt-3 text-sm text-red-400 hidden"></div>
        </form>
        <div class="mt-6 pt-4 border-t border-slate-800/60 text-center text-xs text-slate-500">
            Created by Muvixo
        </div>
    </div>
</div>
<script>
document.getElementById('loginForm').addEventListener('submit', async (e) => {{
    e.preventDefault();
    const btn = e.target.querySelector('button[type="submit"]');
    const err = document.getElementById('errorMsg');
    err.classList.add('hidden');
    btn.disabled = true;
    btn.innerHTML = '<div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div> Signing in...';
    try {{
        const res = await fetch('/api/login', {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{ password: document.getElementById('pw').value }})
        }});
        if (!res.ok) {{
            const data = await res.json().catch(() => ({{}}));
            throw new Error(data.detail || 'Invalid password');
        }}
        location.href = '/dashboard';
    }} catch (e) {{
        err.textContent = e.message;
        err.classList.remove('hidden');
        btn.disabled = false;
        btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" y1="12" x2="3" y2="12"/></svg> Sign In';
    }}
}});
</script>
</body>
</html>"""

# ---------- DASHBOARD_HTML (escaped braces) ----------
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MX-UI v1.0.0</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #070a13; }}
        .glow-effect {{ box-shadow: 0 0 25px rgba(59, 130, 246, 0.12); }}
        .modal-glow {{ box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 50px rgba(59, 130, 246, 0.05); }}
        .circle-chart {{ transition: stroke-dasharray 0.35s ease; transform: rotate(-90deg); transform-origin: 50% 50%; }}
        .custom-modal-overlay {{
            transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.2s, visibility 0.2s;
            visibility: hidden;
            opacity: 0;
            backdrop-filter: blur(0px);
        }}
        .custom-modal-overlay.active {{
            visibility: visible;
            opacity: 1;
            backdrop-filter: blur(12px);
        }}
        .toast {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: #0f172a;
            border: 1px solid #1e293b;
            color: #e2e8f0;
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 13px;
            font-family: Inter, sans-serif;
            opacity: 0;
            transition: opacity 0.25s, transform 0.25s;
            z-index: 9999;
            pointer-events: none;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }}
        .toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
        .toast.success {{ border-color: #22c55e; color: #86efac; }}
        .toast.error {{ border-color: #ef4444; color: #fca5a5; }}
    </style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex flex-col justify-between relative antialiased tracking-tight">

<div class="toast" id="toast"></div>

<!-- Top Navigation -->
<header class="border-b border-slate-800/80 bg-slate-900/40 backdrop-blur-md sticky top-0 z-40">
    <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect">
                <i data-lucide="shield-check" class="w-5 h-5"></i>
            </div>
            <div>
                <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent font-sans">MX-UI PANEL</span>
                <span class="text-xs block text-slate-500 font-medium tracking-normal">v1.0.0 • Core Matrix</span>
            </div>
        </div>
        <div class="flex items-center space-x-4">
            <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                <span class="w-1.5 h-1.5 mr-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                Node Gateway Online
            </span>
            <button onclick="logout()" class="text-slate-400 hover:text-slate-200 text-sm font-medium flex items-center gap-1.5">
                <i data-lucide="log-out" class="w-4 h-4"></i> Logout
            </button>
        </div>
    </div>
</header>

<!-- Main -->
<main class="max-w-6xl w-full mx-auto px-4 py-8 flex-grow">
    <!-- Hardware Diagnostic Rings -->
    <h2 class="text-xs font-bold text-slate-500 uppercase tracking-widest mb-3 px-1">System Diagnostics</h2>
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <!-- CPU -->
        <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="relative w-16 h-16 shrink-0">
                <svg class="w-full h-full" viewBox="0 0 36 36">
                    <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    <path class="text-blue-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center text-[10px] font-mono font-bold text-blue-400" id="ring-cpu-pct">0%</div>
            </div>
            <div class="text-center sm:text-right">
                <p class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">CPU</p>
                <p class="text-lg font-bold mt-0.5 text-slate-100 font-mono" id="ring-cpu-val">0 Cores</p>
            </div>
        </div>
        <!-- RAM -->
        <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="relative w-16 h-16 shrink-0">
                <svg class="w-full h-full" viewBox="0 0 36 36">
                    <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    <path class="text-indigo-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center text-[10px] font-mono font-bold text-indigo-400" id="ring-ram-pct">0%</div>
            </div>
            <div class="text-center sm:text-right">
                <p class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">RAM</p>
                <p class="text-lg font-bold mt-0.5 text-slate-100 font-mono" id="ring-ram-val">0 GB / 0 GB</p>
            </div>
        </div>
        <!-- Swap -->
        <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="relative w-16 h-16 shrink-0">
                <svg class="w-full h-full" viewBox="0 0 36 36">
                    <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    <path class="text-amber-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center text-[10px] font-mono font-bold text-amber-400" id="ring-swap-pct">0%</div>
            </div>
            <div class="text-center sm:text-right">
                <p class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Swap</p>
                <p class="text-lg font-bold mt-0.5 text-slate-100 font-mono" id="ring-swap-val">0 GB / 0 GB</p>
            </div>
        </div>
        <!-- Storage -->
        <div class="bg-slate-900/60 border border-slate-800/70 rounded-2xl p-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="relative w-16 h-16 shrink-0">
                <svg class="w-full h-full" viewBox="0 0 36 36">
                    <path class="text-slate-800" stroke-width="3" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                    <path class="text-rose-500 circle-chart" stroke-dasharray="0, 100" stroke-width="3" stroke-linecap="round" stroke="currentColor" fill="none" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center text-[10px] font-mono font-bold text-rose-400" id="ring-disk-pct">0%</div>
            </div>
            <div class="text-center sm:text-right">
                <p class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">Storage</p>
                <p class="text-lg font-bold mt-0.5 text-slate-100 font-mono" id="ring-disk-val">0 GB / 0 GB</p>
            </div>
        </div>
    </div>

    <!-- Configurations Container -->
    <div class="bg-slate-900 border border-slate-800/80 rounded-2xl overflow-hidden glow-effect">
        <div class="p-6 border-b border-slate-800/80 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 bg-slate-900/40">
            <div>
                <h2 class="text-xl font-bold text-slate-100">V2Ray Inbound Proxies</h2>
                <p class="text-sm text-slate-400 mt-0.5">Manage virtual server bridges, generate QR structures, or modify framework credentials.</p>
            </div>
            <button onclick="toggleModal('inboundModal', true)" class="flex items-center justify-center space-x-2 bg-blue-600 hover:bg-blue-500 text-white font-medium text-sm px-4 py-2.5 rounded-xl transition duration-200 shadow-lg shadow-blue-600/10 shrink-0">
                <i data-lucide="plus" class="w-4 h-4"></i>
                <span>Add New Config</span>
            </button>
        </div>

        <!-- Inbound Node Rows -->
        <div class="divide-y divide-slate-800/60" id="config-list">
            <!-- dynamically loaded -->
        </div>
    </div>
</main>

<!-- Footer -->
<footer class="border-t border-slate-800/60 bg-slate-950 py-4 text-xs text-slate-500">
    <div class="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
        <div class="flex items-center space-x-3">
            <p>MX-UI v1.0.0</p>
            <span class="text-[9px] font-mono font-bold tracking-widest text-slate-400 border border-slate-800 px-1.5 py-0.5 rounded bg-slate-900/60 select-none">
                Muvixo
            </span>
        </div>
        <div class="flex items-center space-x-4">
            <span>Core Clock: <strong class="text-slate-400 font-mono text-[11px]" id="uptime-display">00:00:00</strong></span>
            <span>API Linkage: <strong class="text-emerald-400">Connected</strong></span>
        </div>
    </div>
</footer>

<!-- ===== MODAL: CREATE CONFIG ===== -->
<div id="inboundModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/75">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl overflow-hidden modal-glow">
        <div class="p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40">
            <div class="flex items-center space-x-3">
                <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400 border border-blue-500/20"><i data-lucide="plus-circle" class="w-5 h-5"></i></div>
                <div>
                    <h3 class="text-lg font-bold text-slate-100">Add New Config</h3>
                    <p class="text-xs text-slate-400">Deploy a new VLESS or XHTTP configuration.</p>
                </div>
            </div>
            <button onclick="toggleModal('inboundModal', false)" class="p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition"><i data-lucide="x" class="w-5 h-5"></i></button>
        </div>
        <div class="p-6 max-h-[65vh] overflow-y-auto space-y-5">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Remark / Label</label>
                    <input type="text" id="new-label" placeholder="e.g., US-Reality-HighSpeed" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Protocol</label>
                    <select id="new-protocol" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition font-mono text-xs">
                        <option value="vless-ws">VLESS + WS</option>
                        <option value="xhttp-packet-up">XHTTP (packet-up)</option>
                        <option value="xhttp-stream-up">XHTTP (stream-up)</option>
                    </select>
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Fingerprint (uTLS)</label>
                    <select id="new-fp" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition font-mono text-xs">
                        <option value="chrome">chrome</option>
                        <option value="firefox">firefox</option>
                        <option value="safari">safari</option>
                        <option value="ios">ios</option>
                        <option value="android">android</option>
                        <option value="edge">edge</option>
                        <option value="360">360</option>
                        <option value="qq">qq</option>
                        <option value="random">random</option>
                        <option value="randomized">randomized</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">ALPN (optional)</label>
                    <input type="text" id="new-alpn" placeholder="e.g., h2,http/1.1" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition">
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Traffic Limit (MB)</label>
                    <input type="number" id="new-limit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Expiry (days, 0 = unlimited)</label>
                    <input type="number" id="new-expiry" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition">
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">IP Limit (0 = unlimited)</label>
                    <input type="number" id="new-iplimit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Speed Limit (0 = unlimited)</label>
                    <div class="flex gap-2">
                        <input type="number" id="new-speed" value="0" step="0.5" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-blue-500 transition">
                        <select id="new-speed-unit" class="bg-slate-950 border border-slate-800 rounded-xl px-2 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500 transition font-mono">
                            <option value="MBIT">Mbps</option>
                            <option value="KB">KB/s</option>
                            <option value="MB">MB/s</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end space-x-3">
            <button onclick="toggleModal('inboundModal', false)" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium rounded-xl transition">Cancel</button>
            <button onclick="createConfig()" class="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-sm font-medium rounded-xl transition shadow-lg shadow-blue-600/10">Deploy Config</button>
        </div>
    </div>
</div>

<!-- ===== MODAL: EDIT ===== -->
<div id="editModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/75">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-2xl rounded-2xl overflow-hidden modal-glow">
        <div class="p-6 border-b border-slate-800 flex items-center justify-between bg-slate-900/40">
            <div class="flex items-center space-x-3">
                <div class="p-2 bg-amber-500/10 rounded-lg text-amber-400 border border-amber-500/20"><i data-lucide="edit" class="w-5 h-5"></i></div>
                <div>
                    <h3 class="text-lg font-bold text-slate-100">Modify Configuration: <span id="editNodeTitle" class="text-blue-400">Node</span></h3>
                    <p class="text-xs text-slate-400">Altering production values resets live connection pipelines directly.</p>
                </div>
            </div>
            <button onclick="toggleModal('editModal', false)" class="p-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-xl transition"><i data-lucide="x" class="w-5 h-5"></i></button>
        </div>
        <div class="p-6 space-y-5">
            <input type="hidden" id="edit-uuid">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Remark Label</label>
                    <input type="text" id="edit-label" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition font-mono">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Protocol</label>
                    <select id="edit-protocol" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition font-mono text-xs">
                        <option value="vless-ws">VLESS + WS</option>
                        <option value="xhttp-packet-up">XHTTP (packet-up)</option>
                        <option value="xhttp-stream-up">XHTTP (stream-up)</option>
                    </select>
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Fingerprint</label>
                    <select id="edit-fp" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition font-mono text-xs">
                        <option value="chrome">chrome</option>
                        <option value="firefox">firefox</option>
                        <option value="safari">safari</option>
                        <option value="ios">ios</option>
                        <option value="android">android</option>
                        <option value="edge">edge</option>
                        <option value="360">360</option>
                        <option value="qq">qq</option>
                        <option value="random">random</option>
                        <option value="randomized">randomized</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">ALPN (optional)</label>
                    <input type="text" id="edit-alpn" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition">
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Traffic Limit (MB)</label>
                    <input type="number" id="edit-limit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Expiry (days from now)</label>
                    <input type="number" id="edit-expiry" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition">
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">IP Limit</label>
                    <input type="number" id="edit-iplimit" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Speed Limit</label>
                    <div class="flex gap-2">
                        <input type="number" id="edit-speed" value="0" step="0.5" class="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm font-mono text-slate-200 focus:outline-none focus:border-amber-500 transition">
                        <select id="edit-speed-unit" class="bg-slate-950 border border-slate-800 rounded-xl px-2 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-amber-500 transition font-mono">
                            <option value="MBIT">Mbps</option>
                            <option value="KB">KB/s</option>
                            <option value="MB">MB/s</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="p-4 border-t border-slate-800 bg-slate-950/40 flex items-center justify-end space-x-3">
            <button onclick="toggleModal('editModal', false)" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium rounded-xl transition">Discard</button>
            <button onclick="saveEdit()" class="px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white text-sm font-medium rounded-xl transition shadow-lg shadow-amber-600/10">Commit Changes</button>
        </div>
    </div>
</div>

<!-- ===== MODAL: QR ===== -->
<div id="qrModal" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/75">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-md rounded-2xl overflow-hidden modal-glow p-6 text-center space-y-5">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3 text-left">
            <div>
                <h3 class="text-base font-bold text-slate-100">Client Bridge Mapping</h3>
                <p class="text-xs text-slate-400 font-mono" id="qrTargetLabel">Node-Mapping</p>
            </div>
            <button onclick="toggleModal('qrModal', false)" class="p-1.5 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded-lg transition"><i data-lucide="x" class="w-4 h-4"></i></button>
        </div>
        <div class="mx-auto w-48 h-48 bg-white p-3 rounded-xl shadow-inner flex items-center justify-center border-4 border-slate-800">
            <img id="qrImage" src="" alt="QR Code" class="w-full h-full object-contain">
        </div>
        <div class="bg-slate-950 border border-slate-800/60 rounded-xl p-3 text-left">
            <span class="text-[10px] text-slate-500 block uppercase font-bold tracking-wider mb-1">Target Sync URI Payload</span>
            <p id="qrTextPayload" class="text-[11px] font-mono text-slate-400 break-all line-clamp-2 select-all"></p>
        </div>
        <button onclick="toggleModal('qrModal', false)" class="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 text-xs font-semibold rounded-xl transition">Close View</button>
    </div>
</div>

<!-- ===== ALERT ===== -->
<div id="customAlert" class="custom-modal-overlay fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-sm rounded-2xl overflow-hidden modal-glow p-6 text-center space-y-4">
        <div class="mx-auto w-12 h-12 rounded-full bg-blue-500/10 border border-blue-500/30 fill-none flex items-center justify-center text-blue-400">
            <i id="alertIcon" data-lucide="info" class="w-6 h-6"></i>
        </div>
        <div class="space-y-1">
            <h3 id="alertTitle" class="text-base font-bold text-slate-100">Notification</h3>
            <p id="alertMessage" class="text-xs text-slate-400 leading-relaxed px-2">Pipeline structural modifications updated successfully.</p>
        </div>
        <button onclick="toggleModal('customAlert', false)" class="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 text-xs font-semibold rounded-xl transition">Acknowledge</button>
    </div>
</div>

<script>
lucide.createIcons();

// Modal toggles
function toggleModal(modalId, show) {{
    const target = document.getElementById(modalId);
    if (show) target.classList.add('active');
    else target.classList.remove('active');
}}

// Toast
function toast(msg, type='') {{
    const el = document.getElementById('toast');
    el.textContent = msg;
    el.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(el._timeout);
    el._timeout = setTimeout(() => el.classList.remove('show'), 2500);
}}

// Copy
function copyLink(inputId) {{
    const inp = document.getElementById(inputId);
    inp.select();
    navigator.clipboard.writeText(inp.value);
    triggerAlert('Token Copied', 'Configuration token copied to clipboard.', 'check-circle');
}}

// Alert
function triggerAlert(title, message, iconName) {{
    document.getElementById('alertTitle').textContent = title;
    document.getElementById('alertMessage').textContent = message;
    const icon = document.getElementById('alertIcon');
    icon.setAttribute('data-lucide', iconName);
    lucide.createIcons();
    toggleModal('customAlert', true);
}}

// QR
function openQrModal(label, uriPayload) {{
    document.getElementById('qrTargetLabel').textContent = label;
    document.getElementById('qrTextPayload').textContent = uriPayload;
    const qrImg = document.getElementById('qrImage');
    qrImg.src = 'https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=' + encodeURIComponent(uriPayload);
    toggleModal('qrModal', true);
}}

// Edit modal
function openEditModal(label, protocol, fingerprint, alpn, limit, expiry, iplimit, speed, unit, uuid) {{
    document.getElementById('editNodeTitle').textContent = label;
    document.getElementById('edit-uuid').value = uuid;
    document.getElementById('edit-label').value = label;
    document.getElementById('edit-protocol').value = protocol;
    document.getElementById('edit-fp').value = fingerprint;
    document.getElementById('edit-alpn').value = alpn || '';
    document.getElementById('edit-limit').value = limit;
    document.getElementById('edit-expiry').value = expiry;
    document.getElementById('edit-iplimit').value = iplimit;
    document.getElementById('edit-speed').value = speed;
    document.getElementById('edit-speed-unit').value = unit || 'MBIT';
    toggleModal('editModal', true);
}}

// Logout
async function logout() {{
    await fetch('/api/logout', {{ method: 'POST' }});
    location.href = '/login';
}}

// Fetch and render configs
async function loadConfigs() {{
    try {{
        const res = await fetch('/api/links');
        if (!res.ok) throw new Error('Unauthorized');
        const data = await res.json();
        const links = data.links || [];
        const container = document.getElementById('config-list');
        if (!links.length) {{
            container.innerHTML = '<div class="p-6 text-center text-slate-400">No configurations yet.</div>';
            return;
        }}
        container.innerHTML = links.map(l => {{
            const protoLabels = {{
                'vless-ws': 'VLESS',
                'xhttp-packet-up': 'XHTTP (packet-up)',
                'xhttp-stream-up': 'XHTTP (stream-up)'
            }};
            const proto = l.protocol || 'vless-ws';
            const label = l.label || 'Unnamed';
            const active = l.active && !l.expired;
            const limit = l.limit_bytes === 0 ? '∞' : fmtBytes(l.limit_bytes);
            const used = fmtBytes(l.used_bytes || 0);
            const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
            const color = pct > 90 ? '#ef4444' : pct > 70 ? '#f59e0b' : '#3b82f6';
            let speedDisplay = '∞';
            if (l.speed_limit_bytes && l.speed_limit_bytes > 0) {{
                speedDisplay = (l.speed_limit_bytes * 8 / 1024 / 1024).toFixed(1) + ' Mbps';
            }}
            return `
            <div class="p-6 hover:bg-slate-800/10 transition duration-150">
                <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
                    <div class="flex items-start space-x-4">
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-bold bg-blue-500/10 text-blue-400 border border-blue-500/20 uppercase tracking-wide mt-1 font-mono">${{protoLabels[proto] || proto}}</span>
                        <div>
                            <div class="flex items-center space-x-2">
                                <h3 class="text-base font-semibold text-slate-200">${{label}}</h3>
                                <span class="text-[10px] px-1.5 py-0.5 text-emerald-400 bg-emerald-500/5 rounded border border-emerald-500/20 font-medium ${{active ? '' : 'hidden'}}">Active</span>
                                <span class="text-[10px] px-1.5 py-0.5 text-red-400 bg-red-500/5 rounded border border-red-500/20 font-medium ${{active ? 'hidden' : ''}}">Inactive</span>
                            </div>
                            <div class="grid grid-cols-2 sm:grid-cols-3 gap-x-6 gap-y-1 mt-2 text-xs text-slate-400">
                                <div>Network: <span class="text-slate-300 font-mono">${{proto.includes('ws') ? 'ws' : 'tcp'}}</span></div>
                                <div>Security: <span class="text-slate-300 font-mono">tls</span></div>
                                <div>Expiry: <span class="text-slate-300 font-mono">${{l.expires_at ? new Date(l.expires_at).toISOString().slice(0,10) : 'Unlimited'}}</span></div>
                            </div>
                            <div class="mt-2 flex items-center gap-4 text-xs text-slate-400">
                                <span>Usage: <span class="text-slate-300 font-mono">${{used}} / ${{limit}}</span></span>
                                <span>IP Limit: <span class="text-slate-300 font-mono">${{l.ip_limit || '∞'}}</span></span>
                                <span>Speed: <span class="text-slate-300 font-mono">${{speedDisplay}}</span></span>
                            </div>
                            <div class="w-full max-w-xs mt-1.5 h-1.5 bg-slate-800/60 rounded-full overflow-hidden">
                                <div class="h-full rounded-full" style="width: ${{pct}}%; background: ${{color}};"></div>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-wrap items-center gap-2 lg:justify-end">
                        <div class="relative flex-grow sm:flex-grow-0 min-w-[260px] max-w-xs">
                            <input type="text" id="uri-${{l.uuid}}" readonly value="${{l.vless_link}}" class="w-full bg-slate-950 border border-slate-800/80 rounded-xl px-3 py-2 pr-10 text-xs font-mono text-slate-400 focus:outline-none select-all truncate">
                            <button onclick="copyLink('uri-${{l.uuid}}')" class="absolute right-2 top-1.5 p-1 text-slate-500 hover:text-slate-300 transition" title="Copy URI"><i data-lucide="copy" class="w-4 h-4"></i></button>
                        </div>
                        <button onclick="openQrModal('${{label}}', '${{l.vless_link}}')" class="p-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 rounded-xl transition" title="QR"><i data-lucide="qr-code" class="w-4 h-4"></i></button>
                        <button onclick="openEditModal('${{label}}','${{proto}}','${{l.fingerprint||'chrome'}}','${{l.alpn||''}}',${{l.limit_bytes || 0}},${{l.expires_at ? Math.ceil((new Date(l.expires_at) - Date.now()) / (86400000)) : 0}},${{l.ip_limit||0}},${{l.speed_limit_bytes ? (l.speed_limit_bytes * 8 / 1024 / 1024) : 0}},'${{l.speed_limit_unit || 'MBIT'}}','${{l.uuid}}')" class="p-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 rounded-xl transition" title="Edit"><i data-lucide="edit-3" class="w-4 h-4"></i></button>
                        <button onclick="deleteConfig('${{l.uuid}}')" class="p-2 bg-red-800/20 hover:bg-red-800/40 border border-red-700/30 text-red-300 rounded-xl transition" title="Delete"><i data-lucide="trash-2" class="w-4 h-4"></i></button>
                    </div>
                </div>
            </div>`;
        }}).join('');
        lucide.createIcons();
        updateStats();
    }} catch (e) {{
        if (e.message.includes('Unauthorized')) location.href = '/login';
    }}
}}

function fmtBytes(b) {{
    if (b === 0) return '0 B';
    if (b < 1024) return b + ' B';
    if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
    if (b < 1024**3) return (b/1024**2).toFixed(2) + ' MB';
    return (b/1024**3).toFixed(2) + ' GB';
}}

async function updateStats() {{
    try {{
        const res = await fetch('/stats');
        const d = await res.json();
        document.getElementById('uptime-display').textContent = d.uptime || '00:00:00';
        // CPU
        const cpuPct = d.cpu_percent || 0;
        const cpuCores = d.cpu_cores || 0;
        document.getElementById('ring-cpu-val').textContent = cpuCores + ' Cores';
        document.getElementById('ring-cpu-pct').textContent = cpuPct.toFixed(1) + '%';
        const cpuCircle = document.querySelector('.text-blue-500.circle-chart');
        if (cpuCircle) cpuCircle.setAttribute('stroke-dasharray', Math.round(cpuPct) + ', 100');
        // RAM
        const ramUsed = d.ram_used_mb || 0;
        const ramTotal = d.ram_total_mb || 1;
        const ramPct = d.ram_percent || 0;
        document.getElementById('ring-ram-val').textContent = (ramUsed/1024).toFixed(2) + ' GB / ' + (ramTotal/1024).toFixed(2) + ' GB';
        document.getElementById('ring-ram-pct').textContent = ramPct.toFixed(1) + '%';
        const ramCircle = document.querySelector('.text-indigo-500.circle-chart');
        if (ramCircle) ramCircle.setAttribute('stroke-dasharray', Math.round(ramPct) + ', 100');
        // Swap
        const swapUsed = d.swap_used_mb || 0;
        const swapTotal = d.swap_total_mb || 1;
        const swapPct = d.swap_percent || 0;
        document.getElementById('ring-swap-val').textContent = (swapUsed/1024).toFixed(2) + ' GB / ' + (swapTotal/1024).toFixed(2) + ' GB';
        document.getElementById('ring-swap-pct').textContent = swapPct.toFixed(1) + '%';
        const swapCircle = document.querySelector('.text-amber-500.circle-chart');
        if (swapCircle) swapCircle.setAttribute('stroke-dasharray', Math.round(swapPct) + ', 100');
        // Storage
        const diskUsed = d.disk_used_gb || 0;
        const diskTotal = d.disk_total_gb || 1;
        const diskPct = d.disk_percent || 0;
        document.getElementById('ring-disk-val').textContent = diskUsed.toFixed(2) + ' GB / ' + diskTotal.toFixed(2) + ' TB';
        document.getElementById('ring-disk-pct').textContent = diskPct.toFixed(1) + '%';
        const diskCircle = document.querySelector('.text-rose-500.circle-chart');
        if (diskCircle) diskCircle.setAttribute('stroke-dasharray', Math.round(diskPct) + ', 100');
    }} catch(e) {{ console.error(e); }}
}}

async function createConfig() {{
    const label = document.getElementById('new-label').value.trim() || 'New Config';
    const protocol = document.getElementById('new-protocol').value;
    const fp = document.getElementById('new-fp').value;
    const alpn = document.getElementById('new-alpn').value.trim();
    const limitMB = parseFloat(document.getElementById('new-limit').value) || 0;
    const expiryDays = parseInt(document.getElementById('new-expiry').value) || 0;
    const ipLimit = parseInt(document.getElementById('new-iplimit').value) || 0;
    const speedVal = parseFloat(document.getElementById('new-speed').value) || 0;
    const speedUnit = document.getElementById('new-speed-unit').value;

    const body = {{
        label,
        protocol,
        fingerprint: fp,
        alpn,
        limit_value: limitMB,
        limit_unit: 'MB',
        expires_days: expiryDays,
        ip_limit: ipLimit,
        speed_limit_value: speedVal,
        speed_limit_unit: speedUnit
    }};

    try {{
        const res = await fetch('/api/links', {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify(body)
        }});
        if (!res.ok) throw new Error('Failed');
        toggleModal('inboundModal', false);
        toast('Config created successfully', 'success');
        loadConfigs();
        document.getElementById('new-label').value = '';
        document.getElementById('new-alpn').value = '';
        document.getElementById('new-speed').value = '0';
    }} catch(e) {{
        toast('Error creating config', 'error');
    }}
}}

async function saveEdit() {{
    const uuid = document.getElementById('edit-uuid').value;
    const label = document.getElementById('edit-label').value.trim();
    const protocol = document.getElementById('edit-protocol').value;
    const fp = document.getElementById('edit-fp').value;
    const alpn = document.getElementById('edit-alpn').value.trim();
    const limitMB = parseFloat(document.getElementById('edit-limit').value) || 0;
    const expiryDays = parseInt(document.getElementById('edit-expiry').value) || 0;
    const ipLimit = parseInt(document.getElementById('edit-iplimit').value) || 0;
    const speedVal = parseFloat(document.getElementById('edit-speed').value) || 0;
    const speedUnit = document.getElementById('edit-speed-unit').value;

    const body = {{
        label,
        protocol,
        fingerprint: fp,
        alpn,
        limit_value: limitMB,
        limit_unit: 'MB',
        expires_days: expiryDays,
        ip_limit: ipLimit,
        speed_limit_value: speedVal,
        speed_limit_unit: speedUnit
    }};

    try {{
        const res = await fetch('/api/links/' + uuid, {{
            method: 'PATCH',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify(body)
        }});
        if (!res.ok) throw new Error('Failed');
        toggleModal('editModal', false);
        toast('Config updated', 'success');
        loadConfigs();
    }} catch(e) {{
        toast('Error updating config', 'error');
    }}
}}

async function deleteConfig(uuid) {{
    if (!confirm('Delete this configuration?')) return;
    try {{
        const res = await fetch('/api/links/' + uuid, {{ method: 'DELETE' }});
        if (!res.ok) throw new Error('Failed');
        toast('Config deleted', 'success');
        loadConfigs();
    }} catch(e) {{
        toast('Error deleting', 'error');
    }}
}}

// Initial load
loadConfigs();
setInterval(updateStats, 5000);
setInterval(loadConfigs, 15000);

</script>
</body>
</html>"""

# ---------- SUB_INFO_HTML (fixed) ----------
SUB_INFO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Subscription Info · MX-UI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
    theme: {{
        extend: {{
            fontFamily: {{
                sans: ['Inter', 'sans-serif'],
                mono: ['JetBrains Mono', 'monospace'],
            }}
        }}
    }}
}}
</script>
<style>
body {{ background-color: #070a13; }}
.glow-effect {{ box-shadow: 0 0 25px rgba(59, 130, 246, 0.12); }}
</style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex flex-col justify-between relative antialiased tracking-tight">
<div class="max-w-2xl w-full mx-auto px-4 py-10 flex-grow">
    <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-8 backdrop-blur-xl glow-effect">
        <div class="flex items-center gap-3 mb-6">
            <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
            </div>
            <div>
                <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">MX-UI PANEL</span>
                <span class="text-xs block text-slate-500 font-medium">v1.0.0</span>
            </div>
        </div>
        <h2 class="text-xl font-bold text-slate-100 mb-1">Subscription Details</h2>
        <p class="text-sm text-slate-400 mb-6">Information for your configuration</p>

        <div class="space-y-4">
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Label</span>
                <span class="font-mono text-slate-200">{label}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Subscription ID (UUID)</span>
                <span class="font-mono text-slate-200 text-sm">{uuid}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Used</span>
                <span class="font-mono text-slate-200">{used_fmt}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Limit</span>
                <span class="font-mono text-slate-200">{limit_fmt}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Expiry</span>
                <span class="font-mono text-slate-200">{expires_at}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Status</span>
                <span class="font-mono text-slate-200">{'Active' if active else 'Inactive'}</span>
            </div>
        </div>

        <div class="mt-6 p-4 bg-slate-950/60 border border-slate-800/60 rounded-xl">
            <p class="text-xs text-slate-400 mb-2">VLESS Link (copy to client):</p>
            <div class="flex items-center gap-2">
                <input type="text" readonly value="{vless_link}" class="flex-1 bg-slate-950 border border-slate-800/80 rounded-xl px-3 py-2 text-xs font-mono text-slate-400 focus:outline-none select-all truncate">
                <button onclick="navigator.clipboard.writeText('{vless_link}').then(()=>alert('Copied!'))" class="p-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition" title="Copy"><svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></button>
            </div>
        </div>
        <div class="mt-4 p-4 bg-slate-950/60 border border-slate-800/60 rounded-xl">
            <p class="text-xs text-slate-400 mb-2">Subscription URL (for clients):</p>
            <div class="flex items-center gap-2">
                <input type="text" readonly value="{sub_url}" class="flex-1 bg-slate-950 border border-slate-800/80 rounded-xl px-3 py-2 text-xs font-mono text-slate-400 focus:outline-none select-all truncate">
                <button onclick="navigator.clipboard.writeText('{sub_url}').then(()=>alert('Copied!'))" class="p-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition" title="Copy"><svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></button>
            </div>
        </div>
        <div class="mt-8 text-center text-xs text-slate-500 border-t border-slate-800/60 pt-4">
            {watermark}
        </div>
    </div>
</div>
<footer class="border-t border-slate-800/60 bg-slate-950 py-3 text-center text-xs text-slate-500">
    {watermark}
</footer>
</body>
</html>"""

# ---------- SUB_USER_HTML (for /sub/user) ----------
SUB_USER_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Subscription · MX-UI</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
    theme: {{
        extend: {{
            fontFamily: {{
                sans: ['Inter', 'sans-serif'],
                mono: ['JetBrains Mono', 'monospace'],
            }}
        }}
    }}
}}
</script>
<style>
body {{ background-color: #070a13; }}
.glow-effect {{ box-shadow: 0 0 25px rgba(59, 130, 246, 0.12); }}
</style>
</head>
<body class="font-sans text-slate-200 min-h-screen flex flex-col justify-between relative antialiased tracking-tight">
<div class="max-w-2xl w-full mx-auto px-4 py-10 flex-grow">
    <div class="bg-slate-900/80 border border-slate-800/80 rounded-2xl p-8 backdrop-blur-xl glow-effect">
        <div class="flex items-center gap-3 mb-6">
            <div class="bg-blue-600 p-2 rounded-xl text-white glow-effect">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
            </div>
            <div>
                <span class="font-bold text-lg tracking-wide bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">MX-UI PANEL</span>
                <span class="text-xs block text-slate-500 font-medium">v1.0.0</span>
            </div>
        </div>

        <h2 class="text-2xl font-bold text-slate-100 mb-1">Subscription Info</h2>
        <p class="text-sm text-slate-400 mb-6">Details for your configuration</p>

        <!-- QR Code -->
        <div class="mb-6 flex justify-center">
            <div class="bg-white p-2 rounded-xl shadow-lg">
                <img src="{qr_url}" alt="QR Code" class="w-40 h-40 object-contain">
            </div>
        </div>

        <!-- Details -->
        <div class="space-y-3">
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Subscription ID</span>
                <span class="font-mono text-slate-200 text-sm">{uuid}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Status</span>
                <span class="font-mono text-slate-200">{status}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Downloaded</span>
                <span class="font-mono text-slate-200">{downloaded}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Uploaded</span>
                <span class="font-mono text-slate-200">{uploaded}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Usage</span>
                <span class="font-mono text-slate-200">{usage} / {total_quota}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Total quota</span>
                <span class="font-mono text-slate-200">{total_quota}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Remained</span>
                <span class="font-mono text-slate-200">{remained}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Last Online</span>
                <span class="font-mono text-slate-200">{last_online}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">Expiry</span>
                <span class="font-mono text-slate-200">{expiry}</span>
            </div>
            <div class="flex justify-between border-b border-slate-800/60 pb-2">
                <span class="text-slate-400">IP(s) connected</span>
                <span class="font-mono text-slate-200">{ips}</span>
            </div>
        </div>

        <!-- Name + Quota bar -->
        <div class="mt-6">
            <div class="flex justify-between text-sm">
                <span class="text-slate-300">{label}</span>
                <span class="text-slate-400 font-mono">{used_fmt} / {limit_fmt}</span>
            </div>
            <div class="w-full h-2 bg-slate-800 rounded-full mt-1 overflow-hidden">
                <div class="h-full bg-blue-500 rounded-full" style="width: {usage_pct}%;"></div>
            </div>
        </div>

        <!-- VLESS Link -->
        <div class="mt-6 p-4 bg-slate-950/60 border border-slate-800/60 rounded-xl">
            <p class="text-xs text-slate-400 mb-2">VLESS Link:</p>
            <div class="flex items-center gap-2">
                <input type="text" readonly value="{vless_link}" class="flex-1 bg-slate-950 border border-slate-800/80 rounded-xl px-3 py-2 text-xs font-mono text-slate-400 focus:outline-none select-all truncate">
                <button onclick="navigator.clipboard.writeText('{vless_link}').then(()=>alert('Copied!'))" class="p-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl transition" title="Copy"><svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></button>
            </div>
        </div>

        <div class="mt-8 text-center text-xs text-slate-500 border-t border-slate-800/60 pt-4">
            {watermark}
        </div>
    </div>
</div>
<footer class="border-t border-slate-800/60 bg-slate-950 py-3 text-center text-xs text-slate-500">
    {watermark}
</footer>
</body>
</html>"""
