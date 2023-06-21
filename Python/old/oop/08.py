# 类的成员描述符

#property()函数
#x = property(fget, fset, fdel, doc)

class Person():
	def fget(self):
		return self._name 
		# and self.age

	def fset(self, name):
		self._name = name.upper()
		# self.age = 
	def fdel(self):
		self._name = 'none'

	name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
p1.name = 'zyp'
print(p1.name)
