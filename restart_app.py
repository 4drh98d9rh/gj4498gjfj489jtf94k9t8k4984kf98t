#!/usr/bin/env python3
# restart_app.py - ریستارت خودکار برنامه

import os
import sys
import time
import subprocess
import signal

def restart_application():
    """ریستارت کردن برنامه"""
    print("🔄 Restarting application...")
    
    # پیدا کردن PID فرآیند اصلی
    try:
        # برای محیط Railway
        if os.environ.get("RAILWAY_SERVICE_NAME"):
            print("🚂 Railway environment detected")
            # Railway خودش ریستارت می‌کند
            # فقط یک فایل flag ایجاد می‌کنیم
            with open("/tmp/restart_signal", "w") as f:
                f.write(f"restart_{int(time.time())}")
            print("✅ Restart signal sent to Railway")
            return True
        
        # برای محیط محلی
        # پیدا کردن فرآیند main.py
        result = subprocess.run(
            ["pgrep", "-f", "python.*main.py"],
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid:
                    print(f"📌 Killing process {pid}")
                    os.kill(int(pid), signal.SIGTERM)
                    time.sleep(2)
        
        # اجرای مجدد
        print("🚀 Starting application...")
        subprocess.Popen([sys.executable, "main.py"])
        print("✅ Application restarted successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error during restart: {e}")
        return False

if __name__ == "__main__":
    restart_application()
