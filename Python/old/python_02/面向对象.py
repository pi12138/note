#类
#定义类
class MyClass:
	i = 12345
	def function(self):		#注意这个self,定义类中的方法时，类方法必须包含参数self并且为第一个参数
		return 'hello world'
#类的实例化
x = MyClass()

print("MyClass 类的属性i为：", x.i)
print("MyClass 类的属性function()为：", x.function())

class Student:
	name = ''
	age = 0

	_height = 0
	__weight = 0			#定义私有变量，weight前面有双下划线，在类外无法直接访问
	def __init__(self, name, age, height, weight):		#定义构造函数，init前后均为双下划线
		self.name = name
		self.age = age
		self._height = height
		self.__weight = weight

		print(self.name)
		print(self.age)
		print(self._height)
		print(self.__weight)
		# return self.a * self.b
y = Student('zyp', 20, 178, 70)
print('name=',y.name)
print('age=',y.age)
print('height=', y._height)
# print('weight=', y.__weight)   #

