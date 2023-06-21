import os
import multiprocessing


def info(title):
	print(title)

	print("module name:", __name__)
	print("parent process id:", os.getppid())
	print("process id:", os.getpid())


def f(name):
	info("function f")
	print("hello", name)

if __name__ == "__main__":
	info('function main')
	p = multiprocessing.Process(target = f, args = ('zyp', ))
	p.start()
	p.join()