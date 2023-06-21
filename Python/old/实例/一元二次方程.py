import cmath

# print(cmath.sqrt(16))
# help(cmath.sqrt)

print('请输入abc：')

a = float(input("please input a:"))

b = float(input('please input b:'))

c = float(input('please input c:'))

d = (b ** 2) - (4 * a * c)

if d >= 0:
	d = cmath.sqrt(d)
	x1 = (-b + d)/(2 * a)
	x2 = (-b - d)/(2 * a)
	print('x1={0}   x2={1}'.format(x1, x2))
else:
	print('无解')