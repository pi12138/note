'''
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

解决方案
最简单的过滤序列元素的方法就是使用列表推导。比如：

'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

plus_num = [n for n in mylist if n>0]
minus_num = [n for n in mylist if n<0]

print(plus_num)
print(minus_num)

# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结
# 果集，占用大量内存。如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生
# 过滤的元素。比如：
plus_num = (n for n in mylist if n>0)
print(plus_num)
for i in plus_num:
    print(i, end=' ')


