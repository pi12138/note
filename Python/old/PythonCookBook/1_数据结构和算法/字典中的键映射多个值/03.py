'''
讨论
一般来讲，创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，
那么对于值的初始化可能会有点麻烦，你可能会像下面这样来实现：

'''

from collections import defaultdict

d1 = {}

pairs =[ 
    ['a',[1,2,3]],
    ['b',['a','b','c']]
]


for key, value in pairs:
    if key not in d1:
        d1[key] = []
    d1[key].append(value)
print(d1)

# 如果使用 defaultdict 的话代码就更加简洁了：
d2 = defaultdict(list)
for key, value in pairs:
    d2[key].append(value)
print(d2)