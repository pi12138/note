l1 = [x * x for x in range(5)]	# 放在[]里是列表生成式
g = (x*x for x in range(5))		# 放在()里是生成器


print("l1 type:", type(l1))
print("g  type:", type(g))

# help(next)

# print(next(l1))			# list不是迭代器，无法使用next()函数
# try:
# 	while True:
# 		print(next(g), end = " ")	# g 是一个迭代器，可以使用next()函数
# except StopIteration as e:
# 	# print(e)		
# 	print("StopIteration")

for i in g:					# 迭代器也可以使用for循环查看内容
	print(i, end = " ")