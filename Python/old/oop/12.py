# 变量的三种用法
# 属性的3种方法：
# 			- 1.赋值
# 			- 2.读取
# 			- 3.删除
# 类属性：property
# 应用场景：
# 		- 对变量除了普通的三种操作，还想增加一些附加操作，可以通过property完成
# 		- x = property(fget, fset, fdel, "doc")
class A():
	# name = 'zyp'
	# age = 18
	def __init__(self):
		self.name = 'name'
		self.age = 20

a1 = A()
# print(A.__dict__)
print(a1.__dict__)
print(20 * "*")
print(a1.name)
# print(A.name)
print(20 * "@")

a1.name = 'Name'	#赋值
print(a1.name)		#读取
del a1.name 		#删除
# print(a1.name)		#会报错
print("-" * 20)

class Person():
	def __init__(self):
		self.name = 'zyp'
		self.age = 20
	# 对类变量进行读取操作时进行此功能
	def fget(self):
		print("被读取")
		return self.name
	# 对类变量进行赋值操作时进行此功能
	def fset(self, name):
		self.name = name
		print(self.name)
	# 对类变量进行删除操作时进行此功能
	def fdel(self):
		pass

	name2 = property(fget, fset, fdel, "property案例")

p1 = Person()

print(p1.name)

print(p1.name2)			# 读取类属性
print("-" * 20)

print(p1.__dict__)
print(Person.__dict__)
print("-" * 20)