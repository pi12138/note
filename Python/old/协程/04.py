# 生成器案例
# 在old()函数中，yield负责返回
# 每次遇到yield返回，再次调用会接着上次未执行的继续执行
def old():
	print("step 1")
	yield 1
	print("step 2")
	yield 2
	print("step 3")
	yield 3

o = old()			
one = next(o)# 生成一个生成器对象o
two = next(o)
three = next(o)
# four = next(o)	# 报错StopIteration

print(one, two, three)


def generator1():
	print("yield front")
	yield generator1			# 
	print("yield behind")

	return None

g1 = generator1()
print(next(g1))
# print(next(g1)) 	#打印出"yield behind"会报错StopIteration


# for循环实现斐波那契函数
def fib1(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b, end = " ")
		a, b = b, a+b 		# 与a = b, b = a + b ,效果不同
		n += 1

	return "Done"

fib1(10)

print("")
# for循环调用生成器，实现斐波那契函数
def fib2(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b 		# 与a = b, b = a + b ,效果不同
		n += 1

	return "Done"

g2 = fib2(10)
for i in g2:
	print(i, end = " ")