from lib.core import run_signin
from lib.utils import log

def run(config):
    log("🚀 Root 正式版模式啟動")
    run_signin(config, device="ROOT-Official")
