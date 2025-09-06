import schedule
import time
import threading
from lib.utils import log

def run_schedule(task_func, run_time="09:00"):
    schedule.every().day.at(run_time).do(task_func)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=loop, daemon=True)
    t.start()
    log(f"⏰ 已啟動排程，每日 {run_time} 執行")
