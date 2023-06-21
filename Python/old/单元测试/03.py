class Person:
	"""
	>>> p1 = Person('zyp')
	>>> p1.get_name()
	'zyp'

	"""

	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name


if __name__ == "__main__":
	import doctest
	doctest.testmod()

	print(Person.__doc__)