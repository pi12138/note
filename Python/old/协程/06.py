# yield from案例
# 函数generator1()和generator2()的用法差不多
# generator2()更简洁
def generator1():
	for i in "AB":
		yield i
# l1 = list(generator1())
# print(l1)
g1 = generator1()
print(next(g1))
print(next(g1))

def generator2():			
	yield from "ab"

g2 = generator2()
print(next(g2))
print(next(g2))
