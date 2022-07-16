from interface import App
import scheduler
from logger import logger
from datetime import datetime
from win10toast import ToastNotifier

toast = ToastNotifier()
app = App()
sche = scheduler.get_sched()

INTERVAL_TIME_SECONDS = 60*30

time_to_rest = INTERVAL_TIME_SECONDS


def start_rest():
    global time_to_rest,INTERVAL_TIME_SECONDS
    time_to_rest = INTERVAL_TIME_SECONDS
    logger.info("start to rest....")
    toast.show_toast(title="time to rest", msg="是时候休息一下了~",icon_path=r"notify.png", duration=5)

def frush_label():
    global time_to_rest
    time_to_rest-=1
    app.updatte_process(time_to_rest/INTERVAL_TIME_SECONDS, format_time_str(time_to_rest))

def format_time_str(time_seconds):
    return "    {}分{}秒    ".format(time_seconds//60, time_seconds%60)

def fix_first_rest_time():
    select_start_time = datetime.strptime(app.start_date.get(),'%Y-%m-%d %H:%M:%S').timestamp()
    now_time = datetime.now().timestamp()
    time_difference = int(now_time-select_start_time)
    while time_difference<0:
        time_difference+=INTERVAL_TIME_SECONDS
    time_difference = time_difference%INTERVAL_TIME_SECONDS
    global time_to_rest
    time_to_rest=INTERVAL_TIME_SECONDS-time_difference


def start_sche():
    fix_first_rest_time()
    sche.remove_all_jobs()
    sche.add_job(start_rest, 'interval', seconds=INTERVAL_TIME_SECONDS, start_date=app.start_date.get(), end_date=app.end_date.get())
    sche.add_job(frush_label, 'interval', seconds=1, start_date=app.start_date.get(), end_date=app.end_date.get())
    if not sche.running:
        sche.start()
        logger.info("job init success...")
    else:
        logger.info("job reset success...")



app.job_callback = start_sche

app.mainloop()