import threading
import asyncio


@asyncio.coroutine
def hello():
    print("hello world! {}".format(threading.currentThread()))
    yield from asyncio.sleep(3)
    print('hello world again! {}'.format(threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()