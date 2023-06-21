# 类的内置属性
#		__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#		__doc__ :类的文档字符串
#		__name__: 类名
#		__module__: 类定义所在的模块（类的全名是'__main__.className'，
#					如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#		__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
#		

class A():
	'''
	这是一个说明文档

	'''
	name = 'no'
	age = 20
	def __init__(self):
		print(name)

print(A.__dict__)
print(A.__doc__)
print(A.__name__)
print(A.__module__)
print(A.__bases__)