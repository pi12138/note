import threading

sum = 0
loopsum = 100000	# loopsum >= 100000

# 申请一把锁，返回一个锁对象
lock = threading.Lock()

def myAdd():
	global sum, loopsum

	for i in range(1, loopsum):
		# 上锁
		lock.acquire() 
		sum += 1
		# 释放锁
		lock.release()


def myMinus():
	global sum, loopsum

	for i in range(1,loopsum):
		lock.acquire()
		sum -= 1
		lock.release()

def main():

	t1 = threading.Thread(target = myAdd, args = ())
	t2 = threading.Thread(target = myMinus, args = ())

	t1.start()
	t2.start()

	t1.join()
	t2.join()


if __name__ == '__main__':

	print("start sum:{0}".format(sum))
	main()

	print('end   sum:{0}'.format(sum))