# 协程案例1

def simple_coroutline():
	print("-> start")
	x = yield 9999				# yield 返回9999
	print("-> received ", x)

# 主程序
try: 
	sc = simple_coroutline()   # 生成一个协程/生成器
	print(1111)
	# sc.send(None)
	# 可以使用sc.send(None),效果一样
	ret1 = next(sc)		# 预激，并且接收yield返回结果
	print(ret1)
	print(2222)
	sc.send("coroutline")

except StopIteration as e:
	print(e)
# 协程案例2，协程的状态
def simple_coroutline2(a):
	print("-> start")
	b = yield a 					# 返回a
	# print("-> received a:", a)
	print("-> received a, b:", a, b)
	c = yield b + a  				# 返回b + a
	print("-> received a, b, c:", a, b, c)

try:
	sc = simple_coroutline2(5)
	ret1 = next(sc)
	print(ret1)
	ret2 = sc.send(6)
	print(ret2)
	ret3 = sc.send(7)
	print(ret3)
except StopIteration as e:
	print(e)
