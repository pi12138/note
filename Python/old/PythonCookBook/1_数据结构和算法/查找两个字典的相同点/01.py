'''
问题
怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

解决方案
考虑下面两个字典：
'''

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 交集操作
equal_keys = a.keys() & b.keys()
print(equal_keys)
equal_dict = a.items() & b.items()
print(equal_dict)
# 并集操作
merge_keys = a.keys() | b.keys()
print(merge_keys)
# 差集
difference = a.keys() - b.keys()
print(difference)
