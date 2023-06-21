#函数
def hello_world():				#定义一个函数
	print("hello world")

hello_world()					#调用函数

# name = input("input name:")
# def hello(name):
# 	print("hello {0}".format(name))

# hello(name)

# number1 = input("number1:")
# number2 = input("number2:")
# number1 = float(number1)
# number2 = float(number2)
# def multiplication(number1, number2):
# 	return number1 * number2 
# print(multiplication(number1, number2))

#简单计算器
# num1 = float(input("num1:"))
# operator = input("operator:")
# num2 = float(input("num2:"))
# def Calculator(num1, num2, operator):
# 	if operator == "+":
# 		print("{0}+{1}={2}".format(num1, num2, num1 + num2))
# 	elif operator == "-":
# 		print("{0}-{1}={2}".format(num1, num2, num1 + num2))
# 	elif operator == "*":
# 		print("{0}*{1}={2}".format(num1, num2, num1 * num2))
# 	elif operator == "/":
# 		print("{0}/{1}={2}".format(num1, num2, num1 / num2))
# 	else:
# 		print("输入运算符有误!")
# Calculator(num1, num2, operator)

#关键字参数
def function1(name = "no", age = 0, sex = "no"):
	print("name:", name)
	print("age:", age)
	print("sex:", sex)
function1()
function1('zyp', 20, 'man')
function1(name = 'zyp', age = 20, sex = 'man')

#