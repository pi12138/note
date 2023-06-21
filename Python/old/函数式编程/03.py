# map举例
# 将一个列表里的每一个元素都乘以10，并返回一个新的列表

list1 = [i for i in range(0, 10)]

list2 = [i * 10 for i in range(0, 10)]	# 列表生成式写法

print("list1:", list1)
print("list2:", list2)

list3 = []								# for循环写法
for i in list1:
	list3.append(i * 10)

print("list3:", list3)

def func1(i):							# map()函数实现写法
	return i * 10

list5 = list(map(func1, list1))
print("list5:", list5)
# help(map)
