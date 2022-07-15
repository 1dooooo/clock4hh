import time
from apscheduler.schedulers.background import BackgroundScheduler



sched = None

# def my_job(args):
#     print(args)
# sche.add_job(my_job, 'interval', seconds=1, args=['学会了'])

def start():
    if sched==None:
        get_sched()
    sched.start()

def get_sched() -> BackgroundScheduler:
    global sched
    sched = BackgroundScheduler()
    return sched
