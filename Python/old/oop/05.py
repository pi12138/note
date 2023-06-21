# 单继承和多继承
## 菱形继承/钻石继承问题：多个子类继承同一个父类，这些子类又被同一个类继承，于是继承关系形成一个菱形
## MRO列表的计算原则：
####	- 子类永远在父类前面
####	- 如果多个父类，则根据继承语法中括号内类的书写顺序存放
####	- 如果多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父亲的父类
class Fish():
	def __init__(self, name):
		self.name = name
	def swim(self):
		print("swimming.....")

class Bird():
	def __init__(self, name):
		self.name = name
	def fly(self):
		print("fiying.....")

class Person():
	def __init__(self, name):
		self.name = name
	def work(self):
		print("working......")

class SuperMan(Person, Bird, Fish):		#多继承
	def __init__(self, name):
		self.name = name

class Student(Person):					#单继承
	def __init__(self, name):
		self.name = name


s1 = SuperMan('zyp')
s1.fly()
s1.swim()
print(SuperMan.__mro__)

s2 = Student('gzy')
s2.work()


## 菱形继承
class A():
	pass

class B(A):
	pass

class C(A):
	pass

class D(B, C):
	pass

print(D.__mro__)


## 
class E():
	pass

class F(E):
	pass

class G(D, F):
	pass

print(G.__mro__)