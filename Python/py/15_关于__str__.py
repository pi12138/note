class Person1:
	def __init__(self, name=None, age=20):
		self.name = name
		self.age = age

	def __str__(self):
		return "{}, {}".format(self.name, self.age)

class Person2:
	def __init__(self, name=None, age=20):
		self.name = name
		self.age = age

class Person3:
	def __init__(self, name=None, age=20):
		self.name = name
		self.age = age

	def __str__(self):
		return "__str__"


if __name__ == "__main__":
	p1 = Person1('zyp', 20)
	p2 = Person2('aaa', 23)
	p3 = Person3("bbb", 30)

	print(p1)
	print(p2)
	print(p3)

