import threading

sum = 0
loopsum = 100000	# loopsum >= 100000


def myAdd():
	global sum, loopsum

	for i in range(1, loopsum):
		sum += 1


def myMinus():
	global sum, loopsum

	for i in range(1,loopsum):
		sum -= 1

def main():

	t1 = threading.Thread(target = myAdd, args = ())
	t2 = threading.Thread(target = myMinus, args = ())

	t1.start()
	t2.start()

	t1.join()
	t2.join()


if __name__ == '__main__':

	# 每次输出结果可能不同
	print("start sum:{0}".format(sum))
	main()

	print('end   sum:{0}'.format(sum))