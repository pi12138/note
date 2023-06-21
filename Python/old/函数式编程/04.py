from functools import reduce
# reduce案例


def func1(x, y):
	return x * y

list1 = [i for i in range(1, 10)]
print("list1:", list1)
# help(reduce)
num1 = reduce(func1, list1)		# 可以用来求阶乘
print("num1:", num1)

def func2(x, y):
	return x + y

num2 = reduce(func2, range(0, 100))
print("num2:", num2)

