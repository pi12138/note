'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

'''

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
	loop1()
	loop2()
	print('end time {}'.format(time.ctime()))

if __name__ == '__main__':
	main()

# main()函数需要5s+3s运行时间