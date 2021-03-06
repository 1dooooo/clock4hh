import logging


logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='clock.log',
    filemode='a',
    encoding="utf8",)
logging.getLogger("apscheduler").setLevel(logging.WARNING)

logger = logging.getLogger("clock")
