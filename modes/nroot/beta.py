from lib.core import run_signin
from lib.utils import log
import time

def run(config):
    log("🧪 No-Root 測試版模式啟動")
    log("⏳ 關閉螢幕後等待 10 秒再開始運作")
    time.sleep(10)
    run_signin(config, device="NoROOT-Beta")
