# 类的常用魔术方法
# 操作类：
# 		- 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
#		- 统一特征：方法名被前后个两个下划线包裹，最常用 __init__(self)
#		- __call__ :在对象当函数使用时触发
#		- __str__:当把对象当字符串使用时自动调用,返回一个字符串
#		- __repr__: 返回字符串，跟__str__类似

# 描述符相关：
# 		- __set__:
# 		- __get__:
# 		- __delete__:

# 属性相关操作
# 		- __getattr__: 访问一个不存在的属性时触发
# 		- __setattr__: 对成员属性进行设置时触发 
# 						__setattr__(self, set_attribute_name, set_attribute_value)

# 运算类相关
#		- __gt__: 进行对象之间大于判断时触发函数，返回值可以是任意值，推荐返回一个bool值
#					__gt__(self, second_object)	 

class A():
	name = 'none'
	age = 20

	def __init__(self, name = 0):
		print("__init__被调用")

	def __call__(self):
		print("__call__在对象当函数使用时被调用！")

	def __str__(self):
		return '把对象当字符串使用时自动调用'

	def __getattr__(self, attr):
		print("找不到该变量:{0}".format(attr))


a = A()
a()
print(a)
print(a.name)
print(a.age)
print(a.attr)		#因为该变量不存在，最后会打印出一个None
# a.attr


class Person():
	def __init__(self):
		pass

	def __setattr__(self, AttrName, AttrValue):
		print("设置属性{0}:{1}".format(AttrName, AttrValue))
		# self.AttrName = AttrValue  			# 会导致死循环，前面函数已经赋值了，不用再次赋值
		# 在此情况下，为了避免死循环，规定统一调用父类魔法函数
		super().__setattr__(AttrName, AttrValue)	#*********

p1 = Person()
print(p1.__dict__)
p1.age = 20
print(p1.__dict__)

# __gt__ 案例
class Student():
	def __init__(self, name):
		self.name = name

	def __gt__(self, object2):
		print("{0} > {1} ?".format(self.name, object2.name))
		return self.name > object2.name

s1 = Student("one")
s2 = Student("two")
print(s1 > s2)
