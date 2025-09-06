from lib.utils import log
from . import official, beta

def menu(config):
    log("📋 Root 模式選單")
    print("1. 正式版")
    print("2. 測試版")
    choice = input("請選擇: ")
    if choice == "1":
        official.run(config)
    elif choice == "2":
        beta.run(config)
    else:
        log("❌ 無效選項", "ERROR")
