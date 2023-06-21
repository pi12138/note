'''问题
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

解决方案
为 了 能 控 制 一 个 字 典 中 元 素 的 顺 序， 你 可 以 使 用 collections 模 块 中 的OrderedDict 类。在迭代操作的时候它会保持元素被插入时的顺序，示例如下：

当你想要构建一个将来需要序列化或编码成其他格式的映射的时候，OrderedDict
是非常有用的。比如，你想精确控制以 JSON 编码后字段的顺序，你可以先使用
OrderedDict 来构建这样的数据：

讨论
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的
元素插入进来的时候，它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会
改变键的顺序。
需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维
护着另外一个链表。所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的
时候（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去），那么你就得仔
细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
'''
from collections import OrderedDict
import json


d1 = OrderedDict()
d2 = {}
# print(d)
d1['name'] = 'zyp'
d1['age'] = 20
d1['sex'] = 'man'
print(d1)

d2['name'] = 'zy'
d2['age'] = 18
d2['sex'] = 'man'
print(d2)

for key in d1:
    print(key, d1[key])


d1_json = json.dumps(d1)
print(d1_json)
d2_json = json.dumps(d2)
print(d2_json)

# 给原有的键重新赋值
d1['name'] = 'gzy'
print(d1)

d2['name'] = 'gyj'
print(d2)

