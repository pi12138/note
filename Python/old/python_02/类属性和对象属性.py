"""
使用类名调用变量只能调用类的属性
生成对象后，使用对象名调用变量只能调用构造函数中的变量
"""

class student(object):
	name = '001'
	age = 20

	def __init__(self):
		self.name = '002'
		self.age = 30

	def __str__(self):
		return self.name

s = student()

print("s.name:", s.name)
print("s.age:", s.age)

print("student.name:", student.name)
print("student.age:", student.age)

# 输出对象时，会调用对象的str方法
print(s)
