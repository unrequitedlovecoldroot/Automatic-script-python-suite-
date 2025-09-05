#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主控程式 (main.py)
功能：
1. 啟動時先詢問是否有 ROOT
2. 提供 ROOT / 無 ROOT / 管理者模式選單
3. 每次執行結束後會回到功能選單
4. 啟動健康檢測
"""

import os
import sys
from lib.utils import load_config, save_config
from lib.utils import clear_screen
from lib.utils import run_health_check
from modes.root import menu as root_menu
from modes.nroot import menu as nroot_menu
from modes.admin import menu as admin_menu

CONFIG_MAIN = "config_main.yaml"


def main_menu():
    """顯示主選單"""
    clear_screen()
    print("==== 自動簽到系統 ====")
    print("1. ROOT 模式")
    print("2. 無 ROOT 模式")
    print("3. 管理者模式")
    print("4. 離開")
    choice = input("請選擇: ").strip()
    return choice


def main():
    # 載入全域設定
    config = load_config(CONFIG_MAIN)

    while True:
        choice = main_menu()

        if choice == "1":
            print("[ROOT 模式] 啟動健康檢測中...")
            run_health_check()
            root_menu.start()
        elif choice == "2":
            print("[無 ROOT 模式] 啟動健康檢測中...")
            run_health_check()
            nroot_menu.start()
        elif choice == "3":
            print("[管理者模式]")
            admin_menu.start()
        elif choice == "4":
            print("再見 👋")
            sys.exit(0)
        else:
            print("無效選項，請重新輸入！")


if __name__ == "__main__":
    main()
