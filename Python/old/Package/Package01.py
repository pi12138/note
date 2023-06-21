# 自定义一个模块 
# 一个类
# 一个函数

class Student():
	def __init__(self, name = "none", age = 0):
		self.name = name
		self.age = age

	def introduce(self):
		print("My name is {0}".format(self.name))

def sayhello():
	print("hello, My name is kkk")

# 此判断语句建议一直作为程序入口
# 可以有效避免模块代码被导入时被动执行的问题
if __name__ == '__main__':
	print("這是自定义模块01")