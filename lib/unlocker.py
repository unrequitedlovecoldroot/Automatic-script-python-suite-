from lib.utils import log
import time

def unlock(device, config):
    unlock_type = config.get("unlock", {}).get("type", "none")
    if unlock_type == "none":
        log("🔓 裝置未設鎖屏")
        return True
    elif unlock_type == "pattern":
        path = config["unlock"]["pattern"]
        log(f"🔓 使用圖形解鎖: {path}")
        time.sleep(2)
        return True
    elif unlock_type == "pin":
        log("🔓 使用 PIN 解鎖")
        time.sleep(2)
        return True
    elif unlock_type == "custom":
        log("🔓 使用自訂座標解鎖")
        time.sleep(2)
        return True
    else:
        log("❌ 未知的解鎖方式", "ERROR")
        return False
