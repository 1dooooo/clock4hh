from interface import app
import scheduler




sche = scheduler.get_sched()


scheduler.start()

app.mainloop()