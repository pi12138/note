import _thread as thread
import time


def loop1():
	print("start loop1 {}".format(time.ctime()))
	time.sleep(5)
	print("end loop1 {}".format(time.ctime()))

def loop2():
	print('start loop2 {}'.format(time.ctime()))
	time.sleep(3)
	print("start loop2 {}".format(time.ctime()))

def main():
	print('start time {}'.format(time.ctime()))

	# 启动多个线程的意思是用多线程去执行某个函数
	# 启动多线程函数是 start_new_thread()
	# 两个参数，第一个参数为函数名，第二个为函数的参数作为元组使用，如果没有则使用空元组
	# 注意：如果函数只有一个参数，需要参数后有一个逗号
	
	thread.start_new_thread(loop1, ())
	thread.start_new_thread(loop2, ())
	print('end time {}'.format(time.ctime()))

if __name__ == '__main__':
	main()
	while True:
		time.sleep(1)
