import math

def yyecfc():
	a = input("请输入a:")
	b = input("请输入b:")
	c = input("请输入c:")

	a = int(a)
	b = int(b)
	c = int(c)

	print("输入的方程为：{0}x2+{1}x+{2}=0".format(a,b,c))

	panduan = b*b - 4*a*c

	if panduan > 0:
		#if math.sqrt(panduan)
		x1 = (-b+math.sqrt(panduan))/(2*a)
		x2 = (-b-math.sqrt(panduan))/(2*a)
		print("x1={0}  x2={1}".format(x1,x2))
	elif panduan == 0:
		x1 = x2 =(-b)/(2*a)
		print("x1=x2={}".format(x1))
	else:
		print("此方程无解！")
yyecfc()