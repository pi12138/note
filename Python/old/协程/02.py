from collections import Iterable
from collections import Iterator

# help(isinstance)

l1 = [1, 2, 3, 4]

bool1 = isinstance(l1, Iterable)
bool2 = isinstance(l1, Iterator)

print("list is Iterable:", bool1)
print("list is Iterator:", bool2)


# 使用iter函数转换
#
s = "string isn't Iterator"

print(isinstance(s, Iterable))
print(isinstance(s, Iterator))

s_iter = iter(s)

print(isinstance(s_iter, Iterable))
print(isinstance(s_iter, Iterator))

help(iter)