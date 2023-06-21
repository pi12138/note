class AgeLimit:
	def __init__(self):
		self.age = 0

	def __get__(self, instance, owner):
		# print("__get__", instance, owner)
		# return instance.__dict__.get(self.age)
		return self.age

	def __set__(self, instance, value):
		# print("__set__", instance, value)
		if value < 0:
			raise ValueError("不能小于0")
		# instance.__dict__[self.age] = value
		self.age = value


class Student:
	name = 0
	age = AgeLimit()
	addr = ""
	phone = ""

	# def __init__(self, name, age, addr, phone):
	# 	self.name = name
	# 	self.age = age
	# 	self.addr = addr
	# 	self.phone = phone


if __name__ == "__main__":
	stu = Student()
	print(stu.__dict__)
	print(stu.age)
	stu.age = 10
	print(stu.__dict__)
	print(stu.age)
	stu.age = -1	# 报错
