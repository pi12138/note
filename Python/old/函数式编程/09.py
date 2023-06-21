import time

# 定义一个装饰器
def PrintTime(func):
	def wrapper(*args, **kwargs):
		print("Time:", time.ctime())
		return func(*args, **kwargs)
	return wrapper


# 使用一个装饰器
# 借助@语法糖
@PrintTime
def hello():
	print("hello world!")

hello()

def func1():
	print("This is func1！")

@PrintTime
def func2():
	print('This is func2!')

func1()
func2()


# 手动执行装饰器
def hello2():
	print("这里手动执行装饰器")

# hello2 = PrintTime(hello2)
# hello2()
# PrintTime(hello2)
f = PrintTime(hello2)
f()							# 会打印两次时间？ 注释掉上面的hello2() = PrintTime(hello2)就可以
							# 只出现一次