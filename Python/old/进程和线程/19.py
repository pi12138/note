import multiprocessing
import time


class ClockProcess(multiprocessing.Process):
	'''
	两个比较重要的函数：
	1. __init__()
	2. run()
	'''
	def __init__(self, interval):
		super().__init__()
		self.interval = interval


	def run(self):
		while True:
			print(time.ctime())
			time.sleep(self.interval)


if __name__ == "__main__":
	p = ClockProcess(5)
	p.start()

	while True:
		print("sleeping.......")
		time.sleep(1)
