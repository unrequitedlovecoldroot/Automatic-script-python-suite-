from lib.utils import log
from lib.unlocker import unlock
from lib.clicker import click
from lib.diary import write_log
from lib.notifier import send_telegram

def run_signin(device, config):
    """
    主流程：
    1. 解鎖裝置
    2. 點擊簽到按鈕
    3. 錯誤處理 & 通知
    4. 日誌紀錄
    """

    log(f"📲 {device} 開始簽到流程")

    try:
        # Step 1: 解鎖
        if not unlock(device, config):
            raise Exception("解鎖失敗")

        # Step 2: 點擊 (支援 ratio / absolute)
        mode = config.get("click_mode", "ratio")
        x = config.get("click", {}).get("x", 0.5)
        y = config.get("click", {}).get("y", 0.5)
        click(x, y, mode)

        # Step 3: 簽到完成
        log("✅ 完成簽到")
        write_log(device, "完成簽到")

        # Step 4: 發送通知 (可選)
        if config.get("notify", {}).get("telegram", False):
            token = config["notify"]["telegram"]["token"]
            chat_id = config["notify"]["telegram"]["chat_id"]
            send_telegram(token, chat_id, f"{device} ✅ 簽到完成")

    except Exception as e:
        log(f"❌ 簽到失敗: {e}", "ERROR")
        write_log(device, f"簽到失敗: {e}")

        # 錯誤通知
        if config.get("notify", {}).get("telegram", False):
            try:
                token = config["notify"]["telegram"]["token"]
                chat_id = config["notify"]["telegram"]["chat_id"]
                send_telegram(token, chat_id, f"{device} ❌ 簽到失敗: {e}")
            except:
                log("⚠️ 通知模組失敗", "WARN")
