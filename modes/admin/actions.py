import os
import time
from lib.utils import log, stop_script, load_config, save_config
from lib.diary import clean_old_logs
from lib.utils import install_package

def show_logs():
    log("📖 顯示日誌")
    try:
        with open("/sdcard/signin_log.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        log("❌ 找不到日誌檔", "ERROR")

def health_check(config):
    log("🩺 開始健康檢查")

    # 1. Python 套件檢查
    required = ["requests", "schedule"]
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            log(f"⚠️ 缺少套件 {pkg}，嘗試安裝中...")
            install_package(pkg)

    # 2. Android 依賴檢查
    if os.system("which uiautomator > /dev/null 2>&1") != 0:
        log("⚠️ 系統缺少 uiautomator，請執行: pkg install uiautomator")

    if os.system("which adb > /dev/null 2>&1") != 0:
        log("⚠️ 系統缺少 adb，請執行: pkg install android-tools")

    # 3. 日誌清理
    clean_old_logs()

    log("✅ 健康檢查完成")

def change_device_name(config):
    log("🔧 修改裝置名稱")
    new_name = input("請輸入新的裝置名稱 (限制 20 字): ").strip()
    if len(new_name) > 20:
        log("⚠️ 名稱過長，自動截斷")
        new_name = new_name[:20]

    config["device_name"] = new_name
    save_config(config, "config_main.yaml")
    log(f"✅ 裝置名稱修改完成: {new_name}")

def stop_scripts():
    log("🛑 停止腳本")
    stop_script()
    time.sleep(1)
    log("📌 已嘗試停止腳本 (請確認是否成功)")
