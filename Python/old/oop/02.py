#关于self
class A():
    name = 'zyp'
    age = 20

    def __init__(self):
    	self.name = '周友鹏'
    	self.age = 20

    def say(self):
    	print(self.name)
    	print(self.age)

class B():
	name = 'gzy'
	age = 16

a = A()
#此时系统会默认把a作为第一个参数，传入函数
a.say()

A.say(a)	#此时self被a替换
A.say(A)	#此时self被A替换, 可以打印出类的成员变量

A.say(B)	#此时传入实例B，因为类B中也有name 和age属性，所以不会报错

##以上代码又称，鸭子模型，在c和java中会报错

