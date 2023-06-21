class Person(object):
	def __init__(self, name=None):
		self.name = name

	def get_name(self):
		return self.name


class Student(Person):
	def __init__(self, name):
		self.name = name


if __name__ == "__main__":
	per = Person('zzz')
	stu = Student('zyp')
	print(stu.get_name())