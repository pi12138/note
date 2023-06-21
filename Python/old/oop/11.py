# 类和对象的三种方法
# 	- 1.实例方法
# 			- 需要实例化才能使用
# 			- 类/对象可以拥有像函数一样的方法，这些对象方法与函数的区别只是一个额外的self变量
# 	- 2.静态方法
# 			- 不需要实例化，通过类直接访问
# 			- 要在类中使用静态方法，需在类成员函数前面加上@staticmethod标记符，
# 			以表示下面的成员函数是静态函数。使用静态方法的好处是，不需要定义实例即可使用这个方法。
# 			另外，多个实例共享此静态方法。 

# 	- 3.类方法
# 			- 不需要实例化
# 			- 类方法与普通的成员函数和静态函数有不同之处，在接触的语言中好像也没见过这种语义，
# 			看它的定义： 一个类方法就可以通过类或它的实例来调用的方法, 不管你是用类来调用这个
# 			方法还是类实例调用这个方法,该方法的第一个参数总是定义该方法的类对象。 
#			记住:方法的第一个参数都是类对象而不是实例对象. 
#			按照惯例,类方法的第一个形参被命名为 cls.任何时候定义类方法都不是必须的
#			（类方法能实现的功能都可以通过定义一个普通函数来实现,只要这个函数接受一个类对
#			象做为参数就可以了）.  


# 案例
class Person():
	# 实例方法
	def eat(self):
		print(self)
		print("eating......")
	# 类方法
	@classmethod
	def play(cls):		# 此处定义cls是为了和self区别开
		print(self)
		print("playing.....")
	# 静态方法
	@staticmethod		#声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
	def say():			#使用了静态方法，则不能再使用self
		print("saying....")
# 实例方法使用
p1 = Person()
p1.eat() 
# 类方法使用
Person.play()
p1.play()
# 静态方法使用
Person.say()
p1.say()
