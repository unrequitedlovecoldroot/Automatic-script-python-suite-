from lib.utils import log
import time

def click(x, y, mode="ratio"):
    if mode == "ratio":
        log(f"👆 比例點擊: {x}, {y}")
    else:
        log(f"👆 絕對座標點擊: {x}, {y}")
    time.sleep(1)
