# 可迭代

l1 = [i for i in range(5)]

# list 是可迭代的，但不是迭代器
for i in l1:
	print(i, end = ' ')
print("*" * 20)
# 	range 是个迭代器

for i in range(5):
	print(i, end = ' ')