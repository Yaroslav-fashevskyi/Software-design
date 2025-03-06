import logging
import time
import os

log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(filename='logs/task_log.log', filemode='w', level=logging.INFO,encoding='utf-8')

def run_task():
    start_time = time.time()

    while time.time() - start_time < 60:
        elapsed_time = int(time.time() - start_time)

        if elapsed_time % 5 == 0:
            logging.info(f"Програма працює: {elapsed_time} секунд, Поточний час: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"[DEBUG] Програма працює: {elapsed_time} секунд, Поточний час: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(1)

    logging.error("Task completed")

run_task()

