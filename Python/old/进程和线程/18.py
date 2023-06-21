import multiprocessing
import time

def func(interval):
	while True:
		print(time.ctime())
		time.sleep(interval)

if __name__ == '__main__':
	p = multiprocessing.Process(target = func, args = (5, ))
	p.start()

	while True:
		print("sleeping .......")
		time.sleep(1)