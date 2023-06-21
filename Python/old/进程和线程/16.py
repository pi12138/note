import threading
import time

def func():
	print("func start!")
	time.sleep(4)
	print("func end！")

if __name__ == "__main__":
	# Timer()规定多长时间后运行某个函数
	t = threading.Timer(6, func)
	t.start()

	i = 0
	while i < 10:
		print("{}**********".format(i))
		time.sleep(3)
		i += 1