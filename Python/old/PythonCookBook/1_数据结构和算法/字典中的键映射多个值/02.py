'''
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要
关注添加元素操作了。比如

需要注意的是，defaultdict 会自动为将要访问的键（就算目前字典中并不存在
这样的键）创建映射实体。如果你并不需要这样的特性，你可以在一个普通的字典上使
用 setdefault() 方法来代替。比如：

但是很多程序员觉得 setdefault() 用起来有点别扭。因为每次调用都得创建一个
新的初始值的实例（例子程序中的空列表 [] ）。
'''

from collections import defaultdict

d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['b'].append('1')
print(d1)

# 注意往集合里添加元素不是使用append而是用add
d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add('1')
print(d2)

d3 = {}
d3.setdefault('a',[]).append(1)
d3.setdefault('a',[]).append(2)
d3.setdefault('b',[]).append(1)
print(d3)