'''
另外一个值得关注的过滤工具就是 itertools.compress() ，它以一个 iterable
对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中对
应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候，
这个函数是非常有用的。比如，假如现在你有下面两列数据：

'''

from itertools import compress

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
true_selector = [n>5 for n in counts]

print("true_selector:", true_selector)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

#  compress(data, selectors) --> iterator over selected data
#  |
#  |  Return data elements corresponding to true selector elements.
#  |  Forms a shorter iterator from selected data elements using the
#  |  selectors to choose the data elements.

new_address = list(compress(addresses, true_selector))
print(new_address)

# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。然后
# compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
# 和 filter() 函数类似，compress() 也是返回的一个迭代器。因此，如果你需要得
# 到一个列表，那么你需要使用 list() 来将结果转换为列表类型。
