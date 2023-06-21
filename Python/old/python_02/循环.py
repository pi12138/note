#while 循环
#python 中没有do...while循环
#用while循环求0到九十九相加之和
n = 0
sum1 = 0
while n < 100:
	sum1 = sum1 + n
	n = n + 1
print("sum1:",sum1)

#用for循环求0到99相加之和
m = 0
sum2 = 0
for m in range(0,100):			#range()函数用于
	sum2 = sum2 + m
print("sum2:",sum2)

#使用range()和len()函数遍历一个序列的索引
student1 = ['靳淑佳', '杨浩然', '陈世创', '王畅', '谷嘉欣', '汪雨乐', '王一凡']
for i in range(len(student1)):
	print(i+1, student1[i])

#使用list() 和range（）和tuple()函数创建列表和元组
list1 = list(range(5))
list2 = list(range(0,10))
list3 = list(range(0,99,9))
print(list1)
print(list2)
print(list3)
tuple1 = tuple(range(5))
print(tuple1)

