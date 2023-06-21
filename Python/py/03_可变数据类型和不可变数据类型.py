# 数字, 不可变
num = 1

print(id(num), num)		# > 140704459137136 1

num = 2

print(id(num), num)		# > 140704459137168 2


# 字符串, 不可变
str1 = "abc"

print(id(str1), str1)	# > 2256838773032 abc

str1 = str1 + "d"

print(id(str1), str1)	# > 2256839515416 abcd


# 列表， 可变
list1 = [1, 2, 3]

print(id(list1), list1)	# > 2059406893704 [1, 2, 3]

list1.append(3)

print(id(list1), list1)	# > 2059406893704 [1, 2, 3, 3]


# 字典，可变
dict1 = {"key1": "value1"}

print(id(dict1), dict1)		# > 1853024673728 {'key1': 'value1'}

dict1['key2'] = "value2"

print(id(dict1), dict1)		# > 1853024673728 {'key1': 'value1', 'key2': 'value2'}


# 布尔， 不可变
bool1 = True

print(id(bool1), bool1)		# > 140704458617424 True

bool1 = False

print(id(bool1), bool1)		# > 140704458617456 False