## 继承变量函数查找顺序：
####	优先查找自己得变量，没有则查找父类
####	构造函数如果没有本类中没有定义，则会自动查找调用父类构造函数
####	如果本类有定义，则不再继续向上查找
## 构造函数：
####	在类进行实例化之前进行调用
####	
#
#	super：不是关键字，而是一个类	
####	super的作用是获取MRO(MethodResolusionOrder)列表中的第一个类
####	super跟父类没有关系，但是可以用super调用到父类
####	两种使用方式：1.扩充父类功能	2.

class Animal():
	def __init__(self):
		print("Tish is Animal")
		pass

class Reptile(Animal):
	def __init__(self, name):
		print("Tish is Reptile {0}".format(name))
		pass

class Dog(Reptile):
	# __init__就是构造函数
	# 每次实例化的时候，第一个被自动调用
	# 因为主要工作是进行初始化，所以得名
	def __init__(self, name):
		print("Tish is {0}".format(name))

#实例化时括号内的参数要和构造函数参数匹配，此处是将d1传给self
d1 = Dog('xiaotou')		#实例化时构造函数会被自动调用

class Cat(Reptile):
	pass

c1 = Cat('Cat')		#Cat 没有构造函数，调用父类的构造函数，即Cat的父类Reptile

# c1 = Cat()		#父类构造函数需要两个参数，不传入参数会报错


print(type(super))
# print(help(super))

print(Cat.__mro__)	# mro可以用来查询"家谱"
					# mro是多继承中，用于保存继承顺序的一个列表



