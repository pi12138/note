'''
作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并。比如：
'''
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

new_dict = dict(b)
print("new_dict:", new_dict)

# update更新字典数据时，如果原字典和新字典有key值一样，则value值会被新字典中的value值取代
new_dict.update(a)
# print("a:",a)
print("new_dict:", new_dict)

'''
这样也能行得通，但是它需要你创建一个完全不同的字典对象（或者是破坏现有
字典结构）。同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。比
如：
'''
a['x'] = 100
a['w'] = "new_key"
print("a:", a)
print("new_dict:", new_dict)

'''
ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说
的结果，比如：
'''
from collections import ChainMap
c = ChainMap(a,b)
print("c:",c)

a['x'] = a['x'] * 10
print("c:", c)