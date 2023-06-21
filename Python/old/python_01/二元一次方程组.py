def eyycfcz(): #输入a,b,c 求解二元一次方程组a1*x+b1*y+c1=0,a2*x+b2*y+c2=0
	a1 = input("请输入a1:")
	b1 = input("请输入b1:")
	c1 = input("请输入c1:")
	a2 = input("请输入a2:")
	b2 = input("请输入b2:")
	c2 = input("请输入c2:")

	a1 = int(a1)
	b1 = int(b1)
	c1 = int(c1)
	a2 = int(a2)
	b2 = int(b2)
	c2 = int(c2)

	print("方程1为：{0}x+{1}y+{2}=0".format(a1,b1,c1))
	print("方程2为：{0}x+{1}y+{2}=0".format(a2,b2,c2))

	x = (b2*c1-b1*c2)/(a2*b1-a1*b2)
	y = (-a1*x-c1)/b1

	print("x={0} y={1}".format(x,y))

eyycfcz()