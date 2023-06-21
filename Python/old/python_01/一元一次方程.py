def yyycfc():
	a = input("请输入a:")
	b = input("请输入b:")

	a = int(a)
	b = int(b)
	if b>0:
		print("你输入的方程为：{0}x+{1}=0".format(a,b))
	elif b==0:
		print("你输入的方程为：{0}x=0".format(a))
	else:
		print("你输入的方程为：{0}x{1}=0".format(a,b))
		
	x = (-a)/b
	print("x={0}".format(x))

yyycfc()

