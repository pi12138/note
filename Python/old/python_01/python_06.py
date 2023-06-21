#python变量类型
#1.list(列表)
#list可以更改

l1 = []			#创建一个空列表
print(type(l1))
print(len(l1))

l2 = ['zyp', 20]
print(l2)

l3 = list(['zyp', 20, 'man'])	#创建列表
print(l3)

##分片操作：对列表的指定段进行截取	
###分片操作是生成一个新的list,使用id()函数验证
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4[0:5]) 		#一般情况下包含左边的下标值，不包含右边的下标值
print(l4[:])		#如果下标不写，则左边表示为0，右边表示下标值最大数加一，即到列表最后
print(l4[1:8:2])	#分片可以控制增长幅度，最后一个数字表示增长幅度，默认是1
print(l4[3:100])	#下标可以超出范围，超出后不考虑
print(l4[-1:-7:-1])	#倒过来截取*****,可以用来颠倒列表

l5 = l4[:]
l6 = l4
print("l5=",l5)
print('l6=',l6)
print(id(l4))
print(id(l5))
print(id(l6))

l4[2] = 2
print('l5[2]=', l5[2])		#下标为2的元素未发生改变
print('l6[2]=', l6[2])		#下标为2的元素发生了改变

print('id(l4)=',id(l4))
del l4[2]					#del删除列表l4中下标为2的元素值，而且删除后的列表id不变
print('l4=',l4)
print('id(l4)=',id(l4))

del l4						#删除整个列表
# print(l4)
l7 = ['zyp', 20]
l8 = ['gzy', 16]	
l9 = l7 + l8				#列表相加
print('l9=',l9)

l10 = l9 * 3				#列表乘法，相当与把n个列表相加起来
print('l10=',l10)

print('zy' in l10)			#列表成员资格判断，使用in 和 not in
print('zyp' in l10)
print('zy' not in l10)
## 列表遍历：for in list
information_zyp = ['zyp', 20, '70kg', '178cm']
for i in information_zyp:
	print(i, end=" ")
print("")

## while循环访问list，一般不用while访问list, ****太蠢了****
j = 0
while j < len(information_zyp):
	print(information_zyp[j], end=" ")
	j = j + 1
print("")
## 双层列表
dorm_130 = [['zyp', 20], ['gzy', 16], ['lfs', 21], ['gyj', 20], ['zy', 20], ['kah', 20]]
for name, age in dorm_130:
	print(name, '--', age)
## 列表内涵list content		
dorm_130_1 = [i for i in dorm_130]	
print(dorm_130_1)

m = [x for x in range(0,10)]	#列表生成式
print(m)
n = [x*10 for x in m]
print(n)
mn = [x for x in m if x % 2 == 0]
print(mn)

## list.copy()		#浅拷贝
dorm_130_2 = dorm_130.copy()
print(id(dorm_130))
print(id(dorm_130_2))

#2.tuple
#元组类似与list，但是元组内容不可更改
t1 = ()			#创建一个空tuple
print(t1)

t2 = (1,)		#创建一个只有一个值的元组，注意后面的逗号
print(t2)
print(type(t2))

t3 = (1)		#有无逗号的区别
print(t3)
print(type(t3))

t4 = (1,2,3,4)
print(t4)
## 双层元组遍历
information_zyp_t = (('name', 'zyp'), ('age', 20), ('weight', '70kg'), ('height', '178cm'))
for i in information_zyp_t:
	# print(i)
	for j in i:
		print(j, end=" ")
	print("")

for i, j in information_zyp_t:
	print(i, '---', j)

t5 = (4, 4, 3, 1, 1, 5, 6, 7, 7)
print('max=',max(t5))
print('min=',min(t5))
print('id_max=',id(max(t5)))
print('id_min=',id(min(t5)))
print('id_t5[3]=',id(t5[3]))
print('id_t5[4]=',id(t5[4]))
print('id_t5[7]=',id(t5[7]))
print('id_t5[8]=',id(t5[8]))
# print(id(t5[0]))
# print(id(t5[1]))

## python两个变量交换
x = 100
y = 200

x, y = y, x			#交换x，y之间的值
print('x=', x)
print('y=', y)
#3.set 集合
##一堆确定的无序的唯一的数据
##集合内部只能放置可哈希的数据
s = set()			#创建一个空的集合，只能用set()，不能使用{}
print(type(s))
print(s)

d = {}				#默认为字典
print(type(d))

s1 = {1, 2, 3, 4, 5, 5}			#初始化之后集合会自动过滤掉重复内容
print(type(s1))		#创建有内容的集合
print(s1)

## frozen set :冰冻集合
## 不可进行任何修改的集合
s2 = frozenset()
print(type(s2))
print(s2)


#4.dict 字典
##字典是一种组合数据，没有顺序，数据以键值对形式出现
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
#d = {key1 : value1, key2 : value2 }
##key键必须唯一，而且必须是可哈希的值
##value 可以为任何值
d1 = dict()		#创建空字典
print(d1)

d2 = {'one': 1, 'two': 2, 'three': 3}
print(d2)
print(d2['one'])

for key in d2:			#直接for循环访问，直接按key访问
	print(key, d2[key])

for key in d2.keys():
	print(key, d2[key])

for value in d2.values():
	print(value)

for key, value in d2.items():
	print(key, '---', value)

## 字典生成式
d3 = {key:value for key, value in d2.items() if value % 2 == 0}
print(d3)

list1 = ['zyp', 'gzy', 'lfs']
tuple1 = tuple(list1)
dict1 = dict.fromkeys(list1, 20)
dict2 = dict.fromkeys(tuple1,30)
dict3 = dict.fromkeys(list1)
print(dict1)
print(dict2)
print(dict3)