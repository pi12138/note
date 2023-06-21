#列表里的数据不必全是相同的数据类型

list1 = ['zyp', 'nan', 18, '178cm', '信阳']
print(list1)
print("name=",list1[0])			#按下标访问列表
print("sex=",list1[1])
print("age=",list1[2])
print("height=",list1[3])
print("addr=",list1[4])
print(list1[2:])				#切割列表

list2 = list1 + ['play games', 'sport']		#拼接列表
print(list2)

#python 字符串是固定的，无法改变其某些元素内容，但是列表可以改变其中的元素
list2[2] = 20					#改变指定位置元素值
print(list2)

list2.append('listen to music')
print(list2)
list2.append('play tennis')
print(list2)

print(list2[0:5])

#列表可以修改指定区间的值
list2[0:5] = ['zy', 'nan', 21, '178cm', '南阳']		#替换前五个值
print(list2)

list3 = ['gzy', 'nan', 16, '178cm', '周口']
print(list3)
list3[3:5] = []										#移除第4个到第5个
print(list3)
list3[:] = []										#清空列表
print('list3=',list3)

print("len1=",len(list1))
print("len2=",len(list2))
print("len3=",len(list3))

#列表也可以嵌套
list4 = ['zyp', 'man', 20]
list5 = ['zgq', 'man', 8]
list6 = [list4, list5]
print(list6)										#嵌套列表
print(list6[0][1])