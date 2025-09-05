import os
import subprocess
import datetime
import hashlib

def run_health_check():
    """健康檢查"""
    try:
        import requests
    except ImportError:
        return {
            "ok": False,
            "msg": "缺少套件 requests",
            "install_cmd": "pip install requests"
        }
    return {"ok": True, "msg": "一切正常"}

def log(message, device="default"):
    """記錄日誌 (30 天清理)"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = f"logs/{device}.log"
    os.makedirs("logs", exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
    clean_old_logs(log_file)

def clean_old_logs(log_file):
    """自動清理超過 30 天的日誌"""
    if not os.path.exists(log_file):
        return
    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    cutoff = datetime.datetime.now() - datetime.timedelta(days=30)
    new_lines = []
    for line in lines:
        try:
            ts = line.split("]")[0][1:]
            t = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            if t >= cutoff:
                new_lines.append(line)
        except:
            new_lines.append(line)
    with open(log_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
