def funA():
	print('This is funA()')

funB = funA		# 函数名称是变量
funB()
print(funA)
print(funB)


# 高阶函数举例
# fun1是普通函数，返回一个传入数字的100倍
# fun2把传入参数乘以3倍
def fun1(n):
	return n * 100

def fun2(n):
	return fun1(n) * 3

print(fun2(3))

# 高阶函数
def fun3(n, f):
	return f(n) * 3

print(fun3(4, fun1))