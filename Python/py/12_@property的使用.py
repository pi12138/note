class Student(object):
	def __init__(self, name):
		self._name = name

	def get_name(self):
		return self._name


	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

if __name__ == "__main__":
	stu1 = Student('zyp')

	print(stu1.get_name())
	print(stu1.name)
	stu1.name = 'pyz'
	print(stu1.get_name())
	print(stu1.name)
