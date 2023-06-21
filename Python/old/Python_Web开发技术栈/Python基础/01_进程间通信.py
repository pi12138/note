from multiprocessing import Process, Queue
import os, random, time


def write(q):
	print("Process start write...: {}".format(os.getpid()))
	for value in ['A', 'B', 'C']:
		print("put {} to Process".format(value))
		q.put(value)
		time.sleep(random.random())

def read(q):
	print("Process start read...: {}".format(os.getpid()))
	while True:

		value = q.get(True)
		print("get {} from Process".format(value))
		



if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write, args=(q, ))	
	pr = Process(target=read, args=(q, ))

	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
