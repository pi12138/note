#字典用{}
#创建字典
#定义字典 dictionary = {key1:value1,key2:value2,key3:value3....}
#1.key值唯一，value可以重复
#2.key值不可变，所以列表不能作为key值，可以用数字，字符串或者元组
information = {'name':'周友鹏', 'sex':'man', 'age':20, 'addr':'xinyang'}
print("name:",information['name'])
print("sex:",information['sex'])
print("age:",information['age'])
print("addr:",information['addr'])

#修改字典中的值
information['name'] = '腿哥'
information['age'] = 16
print(information['name'])
print(information['age'])
print(str(information))

#删除单一元素和删除整个字典
del information['addr']
# print(information['addr'])			被删除
print(str(information))
information.clear()						#删除字典里所有元素
print(str(information))
# print(information['name'])  			被删除
del information							#删除字典
# print(str(information))				字典已经被删除无法打印

dictionary1 = {'name':'周友鹏', 'sex':'man', 'age':20, 'addr':'xinyang'}
for k, v in dictionary1.items():
	print(k, "-----", v)
print("#" * 10)

# for k in dictionary1.keys():
# 	for v in dictionary1.values():
# 		print(k, "-----", v)

