import datetime
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def write_log(device, msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(LOG_DIR, f"{device}_log.txt")

    # 保留 30 天內的紀錄
    if os.path.exists(log_path):
        lines = open(log_path, "r", encoding="utf-8").readlines()
        if len(lines) > 5000:  # 假設 5000 行 ≈ 30 天
            lines = lines[-5000:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {msg}\n")
