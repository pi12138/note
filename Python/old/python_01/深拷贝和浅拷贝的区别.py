a = [1, 2, 3, [10, 20, 30]]
b = a.copy()			#浅拷贝,只拷贝一层内容
print('a=',a)
print('b=',b)
print('a_id=',id(a))
print('b_id=',id(b))

print('a[3]_id=',id(a[3]))		#列表[10, 20, 30]的地址未被拷贝
print('b[3]_id=',id(b[3]))

a[3][2] = 22					#修改列表[10, 20, 30],中的内容，a,b均会改变
print('a=',a)
print('b=',b)