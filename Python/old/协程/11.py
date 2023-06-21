from concurrent.futures import ThreadPoolExecutor
import time


def return_future(msg):
	time.sleep(3)
	return msg

# help(ThreadPoolExecutor())
# 创建一个线程池
pool = ThreadPoolExecutor(max_workers = 2)

# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')

# done()：如果调用被成功取消或者完成running返回True
# help(f1.done())
# time.sleep(5)
print(f1.done())
# time.sleep(5)     括号内时间大于上面sleep内的时间就返回true
time.sleep(1)
print(f2.done())


print(f1.result())
print(f2.result())