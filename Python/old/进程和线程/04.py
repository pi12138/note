import threading
import time


def loop1(in1):
	print("start loop1 {}".format(time.ctime()))
	print('这是参数1{0}'.format(in1))
	time.sleep(5)

	print("end loop1 {}".format(time.ctime()))

def loop2(in1, in2):
	print('start loop2 {}'.format(time.ctime()))
	print('这是参数1{0}，这是参数2{1}'.format(in1, in2))
	time.sleep(3)
	print("end loop2 {}".format(time.ctime()))

def main():
	print('start time {}'.format(time.ctime()))
	t1 = threading.Thread(target = loop1, args = (111, ))
	t2 = threading.Thread(target = loop2, args = (111, 222))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	
	print('end time {}'.format(time.ctime()))

if __name__ == '__main__':
	main()
	
