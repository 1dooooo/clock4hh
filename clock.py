from interface import App
import scheduler
from logger import logger
import datetime
import tkinter.messagebox as msgbox
app = App()
sche = scheduler.get_sched()

INTERVAL_TIME_SECONDS = 60*10

time_to_rest = INTERVAL_TIME_SECONDS


def start_rest():
    global time_to_rest,INTERVAL_TIME_SECONDS
    time_to_rest = INTERVAL_TIME_SECONDS
    msgbox.showinfo("该休息了~")
    logger.info("start to rest....")

def my_job():
    global time_to_rest
    time_to_rest-=1
    app.updatte_process(time_to_rest/INTERVAL_TIME_SECONDS, format_time_str(time_to_rest))

def format_time_str(time_seconds):
    return "    {}分{}秒    ".format(time_seconds//60, time_seconds%60)

def start_sche():
    
    sche.remove_all_jobs()
    sche.add_job(start_rest, 'interval', seconds=INTERVAL_TIME_SECONDS, start_date=app.start_date.get(), end_date=app.end_date.get())
    sche.add_job(my_job, 'interval', seconds=1, start_date=app.start_date.get(), end_date=app.end_date.get())
    if not sche.running:
        sche.start()
        logger.info("job init success...")
    else:
        logger.info("job reset success...")
app.job_callback = start_sche

app.mainloop()