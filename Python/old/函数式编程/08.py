
def count():
	list1 = []

	for i in range(1, 4):
		def f():
			return i * i
		# print(f())
		list1.append(f)

	return list1

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def func1(num1):

	print('num1:', num1)
	def func2(num2):
		print('num2:', num2)
		return num1 + num2

	return func2

f2 = func1(20)

print(f2(100))
print(f2(200))

#定义一个函数
def test(number):
 
    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，
    #那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d"%number_in)
        return number+number_in
    #其实这里返回的就是闭包的结果
    return test_in
 
 
#给test函数赋值，这个20就是给参数number
ret = test(20)
 
#注意这里的100其实给参数number_in
print(ret(100))
 
#注意这里的200其实给参数number_in
print(ret(200))


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def func3():
	def func4(i):
		def func5():
			return i * i
		return func5
	list2 = []
	for i in range(1, 4):
		list2.append(func4(i))

	return list2

f4, f5, f6 = func3()
print(f4())
print(f5())
print(f6())
