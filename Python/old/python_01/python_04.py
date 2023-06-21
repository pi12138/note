# #函数
# #def 函数名(参数列表)：
# #	函数体
# # def function():
# # 	print("第一个函数！")
# # 	print("我需要被调用才能使用!")

# # function()

# # def hello(name):
# # 	print("hello,{0}!".format(name))
# # 	return "我不认识你,你哪位{0}".format(name)
# # name = "zyp"
# # ret = hello(name)
# # print(ret)

# # #编写函数打印九九乘法表
# # def multiplication_table():
# # 	for row in range(1,10):
# # 		for col in range(1,row+1):
# # 			print("{0}*{1}={2} ".format(row,col,row*col),end=" ")
# # 		print("")

# # multiplication_table()

# #参数分类
# #---普通参数
# #---默认参数
# #---关键字参数
# #---收集参数

# # def func_name(p1=3,p2=5):    #默认参数定义
# # 	print("p1={0} p2={1}".format(p1,p2))
# # v1 = 100
# # v2 = 200
# # func_name()
# # func_name(v1,v2)
# # func_name(300,500)

# # def student(name,age,addr):
# # 	print("My name is {0},I am {1} years old,I come from {2}".format(name,age,addr))

# # n = "zyp"
# # a = 20
# # ad = "The earth"

# # student(n,a,ad)
# # def student_key(name="no name",age=0,addr="no"): #关键字参数，一一对应不容易出错
# # 	print("My name is {0},I am {1} years old,I come from {2}".format(name,age,addr))
# # 	pass
# # student_key()
# # student_key(age=a,name=n,addr=ad)


# # def student_zwjs(*args):   #收集参数
# # 	print("Hello everyone!")
# # 	print(type(args))   #type()函数用于检测函数类型
# # 	for item in args:
# # 		print(item)

# # student_zwjs("zyp", 20, "nan", "xinyang")
# # student_zwjs("dididi")

# def student_zwjs2( **kwargs):      #收集参数之关键之参数
# 	print(type(kwargs))
# 	for k,v in kwargs.items():
# 		print(k, "-----", v)

# student_zwjs2(name="zyp", age=20, sex="nan", addr="xinyang")
# print("*"*100)

#收集参数混合应用
def student_zwjs3(name, age, *args, hobby="no", **kwargs):
	print("hello everyone!")
	print("My name is {0}, i am {1} years old".format(name, age))
	if hobby == "no":
		print("I don't have hobby!")
	else:
		print("My hobby is {0}".format(hobby))
	print("*" * 20)
	for i in args:
		print(i)
	print("#" * 20)
	for k, v in kwargs.items():
		print(k, "---", v)

name3 = "zyp"
age3 = 20
student_zwjs3(name3, age3)
student_zwjs3(name3, age3, hobby = "paly games")
student_zwjs3("zyp", 20,"xinyang", hobby = "play games", addr = "信阳")