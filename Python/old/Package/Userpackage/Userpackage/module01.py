
class Person():

	def __init__(self, name = 'none', age = 0):
		self.name = name
		self.age = age

	def introduce(self):
		print("My name is {0}, I am {1} years old".format(self.name, self.age))

