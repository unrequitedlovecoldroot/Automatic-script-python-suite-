import requests
from lib.utils import log

def send_telegram(token, chat_id, msg):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": msg}
        requests.post(url, data=data, timeout=5)
        log("📩 Telegram 通知成功")
    except Exception as e:
        log(f"通知失敗: {e}", "WARN")
        with open("notify_fail.log", "a", encoding="utf-8") as f:
            f.write(f"[失敗通知] {msg}\n")
