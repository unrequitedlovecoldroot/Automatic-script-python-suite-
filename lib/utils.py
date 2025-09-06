import yaml
import os
import sys
import time
from colorama import Fore, Style

def load_config(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def save_config(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)

def log(msg, level="INFO"):
    color = {
        "INFO": Fore.GREEN,
        "WARN": Fore.YELLOW,
        "ERROR": Fore.RED
    }.get(level, Fore.WHITE)
    print(f"{color}[{level}] {msg}{Style.RESET_ALL}")

def run_health_check(mode):
    log(f"🔍 健康檢測中 ({mode})", "INFO")
    # 範例檢測：網路
    try:
        import requests
        requests.get("https://www.google.com", timeout=3)
        log("✅ 網路連線正常")
    except:
        log("⚠️ 網路異常，請檢查連線", "WARN")

def stop_if_requested(config):
    stop_cmd = config.get("stop_command", "STOP")
    if os.environ.get("STOP_FLAG") == stop_cmd:
        log("⏹️ 已偵測到停止指令，終止運行", "WARN")
        sys.exit(0)
