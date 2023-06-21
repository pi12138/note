from . import app
import time


@app.task()
def chengfa(x, y):
    time.sleep(8)
    return x * y