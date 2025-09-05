import os
import sys
from lib import utils
from modes.root import menu as root_menu
from modes.nroot import menu as nroot_menu
from modes.admin import menu as admin_menu

def health_check():
    """執行健康檢查"""
    print("🔎 健康檢查中...")
    result = utils.run_health_check()
    if not result["ok"]:
        print(f"❌ 發現問題: {result['msg']}")
        if "install_cmd" in result:
            print(f"👉 請執行: {result['install_cmd']}")
        sys.exit(1)
    print("✅ 健康檢查通過")

def main():
    os.system("clear")
    print("=== 自動簽到程式 ===")
    print("1. ROOT 模式")
    print("2. 無 ROOT 模式")
    print("3. 管理者模式")
    print("0. 離開")

    choice = input("請選擇模式: ")

    health_check()

    if choice == "1":
        root_menu.show()
    elif choice == "2":
        nroot_menu.show()
    elif choice == "3":
        admin_menu.show()
    else:
        print("👋 已退出")
        sys.exit(0)

if __name__ == "__main__":
    main()
