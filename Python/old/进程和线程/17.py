import threading 
import time

num = 0
# mutex = threading.lock()  不使用可重入锁会出现死等现象
mutex = threading.RLock()		# 可重入锁

class MyThread(threading.Thread):
	def run(self):
		global num
		time.sleep(1)

		if mutex.acquire(1):
			num = num + 1
			msg = self.name + ' set num to ' + str(num)
			print(msg)
			mutex.acquire()
			mutex.release()
			mutex.release()



# help(mutex.acquire)

def TestThread():
	for i in range(5):
		t = MyThread()
		t.start()


if __name__ == "__main__":
	TestThread()