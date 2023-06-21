
# enumerate 案例
# help(enumerate)

l1 = [11, 22, 33, 44, 55]

em = enumerate(l1, start = 1) # em = enumerate(l1, 1) 也可以
							  # start 默认为0
print(type(em))
# print(em)
l2 = [i for i in em]
print(l2)