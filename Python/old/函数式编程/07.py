
# 举例 1
def func1():

	def func2():
		print("IN func2")
		return 2

	return func2

f1 = func1()
print(f1())


# 举例2
def func3( *args):
	def func4():
		sum = 0
		for i in args:
			sum = sum + i

		return sum
	return func4
f3 = func3(0, 1, 2, 3, 4, 5)
print(f3())


