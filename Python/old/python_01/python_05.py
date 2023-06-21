# 函数作用域

#变量的作用域
a1 = 1
a2 = 100
def func1():
	# print("a1:",a1)
	# global a1
	a1 = 2				#重名默认访问局部变量

	global a2
	a2 = 200           	#使用global重新定义后，访问全局变量 
	print('a1:',a1)
	print("a2:",a2)

func1()
print('a1:',a1)
print("a2:",a2)
#globals()和locals()函数可以显示全局变量和局部变量，两者均为内建函数
def func2(b1, b2):
	print("locals={0}".format(locals()))		
	# print("global={0}".format(globals()))
func2(100, 200)

#eval()函数:把一个字符串当作一个表达式来执行，返回表达式执行后的结果
#定义eval(string_code, global = None, local = None)

x = 100
y = 200
z = "x * y"
z1 = eval(z)
print("z1:",z1)

#exec()函数:与eval()函数功能类似，但是没有返回值
#exec(string_code, global = None, local = None)
#x = 100
y = 200
z = "x * y"
z2 = exec(z)
print("z2:",z2)

#递归函数
#python对递归深度有限制，超过限制会报错

d1 = 0
def func3():
	global d1
	d1 = d1 + 1
	print(d1)
	if d1 < 10:
		func3()
	else:
		return 0 
func3()

#斐波那契数列
#数学公式：f(1) = 1, f(2) = 1, .....f(n) = f(n-1) + f(n-2)
#例如 1, 1, 2, 3, 5, 8, 13.....
def fib(n):
#n表示第n个数
	if(n > 0):				
		if n == 1:
			return 1

		if n == 2:
			return 1

		return fib(n - 1) + fib(n - 2)
	else:
		print("error!")
print(fib(5))
print(fib(0))

#汉诺塔问题
#规则：1.每次只能移动一个盘子。2.大盘子在下小盘子在上。

def hano(n, a, b, c):
	'''
	汉诺塔递归实现
	n代表几个盘子
	a，b，c均代表塔
	'''

	if n == 1:
		print(a, "-->", c)
		return None
	if n == 2:
		print(a, "-->", b)
		print(a, "-->", c)
		print(b, "-->", c)
		return None
	hano(n - 1, a, c, b)	#把n-1个盘子从a塔借助c塔挪到b塔
	print(a, "-->", c)
	hano(n - 1, b, a, c)	#把n-1个盘子从b塔借助a塔挪到c塔
a = 'A'
b = 'B'
c = 'C'
n = 3
hano(n, a, b, c)


#内置函数id()
i1 = 100
i2 = 200
print(id(i1))
print(id(i2))

i3 = 100
i4 = i1
print(id(i3))
print(id(i4))

i1 = 400
print(id(i1))