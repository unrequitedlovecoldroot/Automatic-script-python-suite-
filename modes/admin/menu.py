from lib.utils import log
from . import actions

def menu(config):
    log("⚙️ 管理員模式選單")
    print("1. 檢視日誌")
    print("2. 健康檢查")
    print("3. 修改裝置名稱")
    print("4. 停止腳本")
    choice = input("請選擇: ")

    if choice == "1":
        actions.show_logs()
    elif choice == "2":
        actions.health_check(config)
    elif choice == "3":
        actions.change_device_name(config)
    elif choice == "4":
        actions.stop_scripts()
    else:
        log("❌ 無效選項", "ERROR")
