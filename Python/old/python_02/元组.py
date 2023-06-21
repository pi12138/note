#元组与列表类似，但是元组内的元素不能修改
#列表使用[],元组使用()

#创建元组
tuple1 = ('zyp', 'man', 20, '信阳')
tuple2 = (1, 2, 3, 4, 5)
tuple3 = 'a', 'b', 'c', 'd','e'

print(tuple1)
print(tuple2[1:5])
print(tuple3)

#创建空元组
tuple4 = ()
print(tuple4)

#tuple中只包含一个元素时，需要在元素后面添加逗号
tuple5 = (1,)
print(tuple5)

#元组元素不可以被修改，但是可以对元组进行拼接
tuple6 = tuple1
tuple7 = ('play games',)
tuple8 = tuple6 + tuple7		#元组拼接
print(tuple8)

#元组元素值无法删除，但是可以使用del删除整个元组
tuple9 = tuple1
print(tuple9)
del tuple9
# print(tuple9)     被删除，无法打印

#判断元素是否存在
tuple10 = ('王畅', '谷嘉欣', '靳淑佳', '王一凡', '汪雨乐', '杨浩然', '陈世创')
name1 = '周友鹏'
name2 = '王一凡'
print(name1 in tuple10)
print(name2 in tuple10)
#打印元组元素
for name in tuple10:
	print(name)
print("*"*10)
#内置函数
tuple11 = (110, 123, 130, 99, 20)
print(max(tuple11))
print(min(tuple11))
print(len(tuple11))
list1 = ['zyp', 'man', 20]
print(list1)
print(tuple(list1))				#将列表转化为元组