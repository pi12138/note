"""
位运算符实现加法第一个add()函数存在递归深度的问题，如果一个正数加负数会出现递归深度的异常，
"""

def add(a, b):
	if b == 0:
		return a
	elif b < 0:
		return a+b
	else:
		return add(a^b, (a&b)<<1)

# 非递归实现, 同样无法计算100+（-100）
def add2(a, b):
	i = a^b
	j = a&b

	while j:
		a = i
		b = j << 1
		i = a^b
		j = a&b

	return i

def subtraction(a, b):
	def opposite(b):
		"""相反数"""
		return ~b+1
	b = opposite(b)
	return add(a, b)


# def 



if __name__ == "__main__":
	print(add(10, 20))
	print(add(10, -20))
	print(add(100, -100))
	print(add(100, -100))
	print(add(100, 200))
	print(subtraction(100, 100))