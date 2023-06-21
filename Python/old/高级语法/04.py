
# deque与list类似，但是有些区别
from collections import deque

q = deque(['a', 'b'])
l1 = ['a', 'b']
# print(dir(list))
# print()
# print(dir(deque))
print(q)
print(l1)

l1.append('c')
q.append('c')

print(l1)
print(q)

# l1.appendleft('d')		# 列表中没有这个内置函数
q.appendleft('d')
print(l1)
print(q)

