from  . import app
import time


@app.task()
def add(x, y):
    time.sleep(4)
    return x + y

