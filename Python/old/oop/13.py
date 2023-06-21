# 抽象
# 	- 抽象方法：没有具体实现内容的方法称为抽象类
# 	- 抽象方法的主要意义是规范了子类的行为和接口
# 	- 抽象类的使用需要借助abc模块
# 	- import abc
# 	
# 	- 抽象类：包含抽象方法的类叫抽象类，通常称为ABC类
#	- 抽象类的使用：
#		- 抽象类可以包含抽象方法，也可以包含具体方法
#		- 抽象类可以有方法也可以有属性
#		- 抽象类不允许直接实例化
#		- 必须继承才能使用，且继承的子类必须实现所有继承来的抽象方法
#		- 如果子类没有实现所有继承的抽象方法，那么子类也不能实例化
#		- 抽象类的主要作用是设定类的标准，以便开发时具有统一的规范

# 抽象方法案例
class Animal():

	def sayhello(self):
		pass

class Person(Animal):
	def sayhello(self):
		print("hello")

class Dog(Animal):
	def sayhello(self):
		print('wangwang')

p1 = Person()
d1 = Dog()

p1.sayhello()
d1.sayhello()
print('-' * 20)

# 抽象类案例
import abc
class Human(metaclass = abc.ABCMeta):

	# 定义抽象方法
	@abc.abstractmethod
	def smoke(self):
		pass
	# 定义类抽象方法
	@abc.abstractclassmethod
	def drink(self):
		pass
	# 定义静态抽象方法
	@abc.abstractstaticmethod
	def play():
		pass

	def sleep(self):
		print('sleeping.....')

