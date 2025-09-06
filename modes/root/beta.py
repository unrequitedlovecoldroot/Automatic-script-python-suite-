from lib.core import run_signin
from lib.utils import log
import time

def run(config):
    log("🧪 Root 測試版模式啟動")
    log("⏳ 等待 5 秒後執行 (測試用延遲)")
    time.sleep(5)
    run_signin(config, device="ROOT-Beta")
