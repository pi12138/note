# 类的相关函数
## 1. issubclass 检查一个类是不是另一个类的子类

class A():
	name = 'none'

class B(A):
	pass

class C():
	pass

print(issubclass(B, A))
print(issubclass(C, A))

## 2. isinstance 检查一个对象是不是一个类的实例

a1 = A()

b1 = B()

print(isinstance(a1, A))
print(isinstance(b1, A))	#？？？？
print(isinstance(b1, C))

## 3. hasattr() 检查对象有没有成员xxx
##	  getattr(): get attribute
##	  setattr(): set attribute
##	  delattr(): delete attribute
print(hasattr(a1, 'name'))
print(hasattr(a1, 'age'))
help(setattr)			#使用help()函数获取帮助

## 4. dir() 获取对象成员列表
print(dir(a1))
print(dir(A))
