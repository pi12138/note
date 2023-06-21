'''
问题
怎样从一个集合中获得最大或者最小的 N 个元素列表？

解决方案
heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
'''

import heapq

list1 = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# def nlargest(n, iterable, key=None):
#     """Find the n largest elements in a dataset.

#     Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
#     """

largest_3 = heapq.nlargest(3, list1)
smallest_3 = heapq.nsmallest(3, list1)

print("largest:",largest_3)
print("smallest:",smallest_3)