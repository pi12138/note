# 列表实现
def fib1(n):
	list1 = [0]

	for i in range(1, n):
		if i == 1 or i == 2:
			list1.append(1)
		else:
			list1.append(list1[i-1] + list1[i-2])
	print(list1)

fib1(10)


# 递归实现
def fib2(max):
	if max == 1 or max == 2:
		return 1
	elif max == 0:
		return 0
	else:
		return fib2(max-1) + fib2(max-2)
for i in range(0, 10):
	print(fib2(i))


# for循环实现
def fib3(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b, end = " ")
		a, b = b, a+b 		# 与a = b, b = a + b ,效果不同
		n += 1

	return "Done"

fib3(10)

# for循环调用生成器，实现斐波那契函数
def fib4(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b 		# 与a = b, b = a + b ,效果不同
		n += 1

	return "Done"

g2 = fib4(10)
for i in g2:
	print(i, end = " ")