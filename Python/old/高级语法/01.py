
# zip 案例
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]

z = zip(l1, l2)

# help(zip)
print(type(z))

for i in z:
	print(i)

l3 = [i for i in z]
print(l3)			# 此处打印为空，注释掉上面的for循环即可正常打印？
					# 设计到可迭代的对象