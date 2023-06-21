# #python 中列表是可变的，但是元组和字符串不能
# list1 = ['zyp','man',20]
# print(list1)			#指定位置插入元素
# for i in list1:
# 	print(i,end = ' ')
# print('')

# addr = '信阳'
# list1.append(addr)			#把一个元素添加到列表的结尾
# print(list1)

# hobby1 = ['play games', 'sport']
# list1.extend(hobby1)			#添加列表来扩展列表
# print(list1)

# list2 = ['zyp','man',20]
# list2.insert(2,addr)			#指定位置插入元素
# print(list2)

# list2.remove('信阳')				#list.remove(x) 删除值为x的第一个元素
# print(list2)

# list3 = ['zyp','man',20]
# # return_pop = list3.pop()
# return_pop = list3.pop(1)		#删除指定元素，并将其返回
# print(list3)
# print(return_pop)

# list4 = list1
# print("list4:",list4)
# list4.clear()					#清空列表里的内容
# print("list4:",list4)

# list5 = list2
# print("list1:",list1)
# print("list5:",list5)
# return_index = list5.index('zyp')		#list.index(x) 返回第一个值为x的元素索引，如果没有则返回一个错误
# print(return_index)

# list6 = [6, 4, 6, 5, 7, 8, 6]
# return_count = list6.count(6)
# print("return_count:",return_count)		#list.count(x) 返回x在列表中出现的次数

# list7 = list6
# list7.sort()							#对列表中的元素进行排序，列表中元素需要是相同的数据类型
# print("list6:",list6)
# print("list7:",list7)
# list7.reverse()							#排倒序
# print("list6:",list6)
# print("list7:",list7)

# list8 = list7.copy()
# print("list8:",list8)
# list8.sort()							#浅复制，对新列表进行操作不会对原有列表产生影响
# print("list7:",list7)
# print("list8:",list8)

# #集合 使用{}创建,基本功能包括关系测试和消除重复元素
# gather1 = {'周友鹏', '周友鹏', '张仪', '高战阳', '雷富山', '郜永健', '孔奥辉'}
# print(gather1)
# gather2 = set('aashjdgbkasgdkasgd')
# gather3 = set('jksahdkasjhdkahdsjka')
# print("gather2:",gather2)
# print("gather3:",gather3)
# print('gather2-gather3:',gather2-gather3)
# print('gather2|gather3:',gather2|gather3)
# print('gather2&gather3:',gather2&gather3)
# print('gather2^gather3:',gather2^gather3)

# #字典
# Transcript = {'王一凡':50, '汪雨乐':50,'谷嘉欣':80, '王畅':80,'靳淑佳':80, '杨浩然':70,'陈世创':70}
# # print(Transcript)
# Name_list = ['王一凡', '汪雨乐', '谷嘉欣', '王畅', '靳淑佳', '杨浩然', '陈世创']
# name = input("输入姓名：")
# if name in Name_list:
# 	print(Transcript[name])
# else:
# 	print("我们班没你这个人！")

# #向字典里添加新项
# QQ = {'1':'1558255789','2':'2059233910'}
# print(QQ)
# QQ['3'] = '3532346870'			#添加新项
# print(QQ)

# #构造函数dict()直接从键值对元组列表中构建字典
# tuple1 = (('name','zyp'), ('age',18), ('sex','man'))
# print("tuple1:",tuple1)
# dict1 = dict(tuple1)
# print("dict1:",dict1)
# print("yes")

# #列表推导式
# list1 = [3, 4, 5]
# list2 = [3*x for x in list1]
# print("list2:",list2)

# list3 = [[x, x*5] for x in list1]
# print("list3:",list3)

# #使用if作为过滤器
# list4 = [3*x for x in list1 if x > 4]
# print("list4:",list4)

# list5 = [3*x for x in list1 if x < 3]
# print("list5:",list5)

# list6 = [3, 4, 5]
# list7 = [6, 7, 8]
# list8 = [x*y for x in list6 for y in list7]
# print("list8:",list8)
# list9 = [list6[i]*list7[i] for i in range(len(list6))]
# print("list9:",list9)

# Pi = 355/113
# print("Pi:",Pi)
# #round()函数返回Pi的四舍五入值
# list10 = [str(round(Pi, j)) for j in range(1,9)]
# print("list10:",list10)

#通过推导式来创建字典
tuple1 = (2, 4, 6)
dict1 = {x: x**x for x in tuple1}
print("dict1:",dict1)

#遍历字典
dict2 = {'name':'zyp', 'sex':'man', 'age':20}
for k, v in dict2.items():
	print(k, '---', v)

#遍历列表，并显示序号使用enumerate()
Name_list = ['王一凡', '汪雨乐', '谷嘉欣', '王畅', '靳淑佳', '杨浩然', '陈世创']
for k, v in enumerate(Name_list):
	print(k,v)

#同时遍历两个列表使用zip()
questions = ['name', 'age', 'hobby']
answers = ['zyp', 20, 'play games']
for q, a in zip(questions, answers):
	print("what is your {0}. It is {1}.".format(q, a))

#反向遍历使用reversed()
for i in reversed(range(1,10,2)):
	print(i,end=" ")
print(" ")
#顺序遍历使用sorted()
fruits = ['orange', 'apple', 'apple', 'pear', 'orange', 'banana']
print('fruits:',fruits)
print("set(fruits):",set(fruits))	#set()函数用来创建集合

for f in sorted(set(fruits)):
	print(f)