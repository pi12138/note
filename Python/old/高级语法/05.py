from collections import defaultdict
# 不使用defaultdict
# 定义一个字典，调用不存在的键值
# 
d1 = {'one':1, 'two':2, 'three':3}
print(d1)
print(d1['one'])
# print(d1['four'])		# 会报错


# 使用defaultdict
#


func = lambda: 'no key'
d2 = defaultdict(func)
# d2 = {'one':1, 'two':2, 'three':3}	# 上面定义d2后，不能使用这种方法给字典赋值？？？
d2['one'] = 1
d2['two'] = 2
 
print(d2)
print(d2['one'])
print(d2['four'])			# 当键值不存在时会执行函数func
# help(defaultdict)