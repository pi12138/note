# 面向对象的三大特性
# 1.封装
## public protected private 不是关键字
## python 私有并不是真的私有，是一种称为name mangling的改名策略
## 可以使用 对象名._ClassName__AttributeName
class Student():
	# public 成员
	name = 'zyp'
	# private 成员
	__age = 20
	# protected 成员
	_height = '178cm'

s1 = Student()
print(s1.name)
# print(s1.__age)		#私有变量无法在类外直接访问，会报错，

print(Student.__dict__)
print(s1.__dict__)

# name mangling策略
print(s1._Student__age)	#通过查找类的__dict__属性查看私有变量名

# print(Student._Student__age) 

# 2.继承
## 一个类获得另一个类中的成员属性和成员方法
## 在python中任何一个类都有一个共同的父类object
## 定义：class Class_Name(BaseClassName)
## 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用，可以用id()函数证明

class Person():
	name = None
	age = 0
	sex = None

	def sleep(self):
		print("sleep")

	def work(self):
		print("make some money!")

class Teacher(Person):

	def MakeTest(self):
		print("MakeTest")

	def sleep(self):
		print("sleeping!")

	def work(self):
		# 扩充父类功能只需要调用相应的父类函数
		## 调用方法1. 父类名.父类成员  2.super().父类成员
		Person.work(self)
		super().work()		#super代表得到父类
		self.MakeTest()

		

print(Person.__dict__)
print(Teacher.__dict__)

t1 = Teacher()
p1 = Person()

print(t1.name)
print(Teacher.name)

print(id(t1.name))		#两者id值一样
print(id(p1.name))

t1.sleep()

t1.work()



















