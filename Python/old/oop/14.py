# 组装类
# 组装类案例
# 1. 使用MethodType
from types import MethodType

class A():
	pass

def say(self):
	print("saying.......")

a = A()
a.say = MethodType(say, A)
a.say()

# help(MethodType)

# 2. 使用type
# 先定义应该具有的成员函数
def eat(self):
	print("eating.....")

def talk(self):
	print("talking....")

# 用type来创建一个类
A = type("AName", (object, ), {'class_eat':eat, 'class_talk':talk})
print(A.__dict__)

a = A()
a.class_talk()
a.class_eat()

print(a.__dict__)

# 3. 使用元类实现 -MetaClass
#		- 元类是类
#		- 被用来创造别的类
#		- 元类写法是固定的，而且必须继承type，命名一般以Metaclass结尾

# 元类使用案例
class PersonMetaClass(type):
	def __new__(cls, name, base, attr):
		# 需要的内容
		attr['id'] = '1615925000'
		attr['address'] = 'Nyist'	

		return type.__new__(cls, name, base, attr)

class Student(metaclass = PersonMetaClass):		# 有元类
	pass
class Teacher():									# 无元类，后面对比
	pass

s1 = Student()

print(s1.id)
print('-'*20)

# 两者对比
print(Student.__dict__)			# 比下面一个多了两个变量id、address
print(Teacher.__dict__)	

# print(s1.__dict__)