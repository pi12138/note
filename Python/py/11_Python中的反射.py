class Person(object):
	age = 100
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name


if __name__ == "__main__":
	p = Person('zyp')
	a = hasattr(p, 'get_name')
	b = hasattr(Person, 'get_name')

	print(a)
	print(b)

	if a:
		print(p.get_name())
	else:
		print("Don't func get_name")


	name = getattr(p, 'get_name')

	print(name())

	print(hasattr(Person, 'age'))
	print(hasattr(p, 'age'))

	setattr(p, 'gender', 'man')
	print(p.gender)
	print(p.name)
	setattr(p, 'name', 'xxx')
	print(p.name)