# 详细内容见廖雪峰网站
import threading
import asyncio

# 使用协程
@asyncio.coroutine
def hello():
	print("hello world {}".format(threading.currentThread()))
	print("start ......{}".format(threading.currentThread()))
	yield from asyncio.sleep(10)
	print("Done  ......{}".format(threading.currentThread()))
	print("hello again!{}".format(threading.currentThread()))

# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
# tasks = [hello(), hello()]
tasks = [hello(), hello(), hello()]
# asyncio使用
loop.run_until_complete(asyncio.wait(tasks))
# 关闭消息循环
loop.close()

# 由上面打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。



