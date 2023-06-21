'''
讨论
列表推导和生成器表达式通常情况下是过滤数据最简单的方式。其实它们还能在
过滤的时候转换数据。比如：

'''
import math

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

new_list = [math.sqrt(n) for n in mylist if n > 0]

print("new_list:", new_list)


'''
过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。比
如，在一列数据中你可能不仅想找到正数，而且还想将不是正数的数替换成指定的数。
通过将过滤条件放到条件表达式中去，可以很容易的解决这个问题，就像这样：

'''
new_list2 = [n if n>0 else 0 for n in mylist]
new_list3 = [n if n<0 else 0 for n in mylist]

print(new_list2)
print(new_list3)
