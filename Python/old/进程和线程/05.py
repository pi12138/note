import time
import threading


def loop1():
	print('start loop1:{0}'.format(time.ctime()))
	time.sleep(5)
	print('end loop1:{0}'.format(time.ctime()))


print('main start!', time.ctime())

t1 = threading.Thread(target = loop1, args = ())
t1.start()

time.sleep(3)

print('main end', time.ctime())