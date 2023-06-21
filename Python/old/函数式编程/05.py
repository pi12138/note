
# filter举例
# 

# help(filter)
def func1(x):
	if x % 2 == 0:
		return x

list1 = [i for i in range(0, 100)]
print("list1:", list1)

list2 = list(filter(func1, list1))
print("list2:", list2)
