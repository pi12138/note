'''
讨论
一般来讲，代码中如果出现大量的硬编码下标值会使得可读性和可维护性大大降
低。比如，如果你回过来看看一年前你写的代码，你会摸着脑袋想那时候自己到底想干
嘛啊。这里的解决方案是一个很简单的方法让你更加清晰的表达代码到底要做什么。
内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
比如：


'''

items = [0, 1, 2, 3, 4, 5, 6]

print('items[2:4] :',items[2:4])

two_four = slice(2,4)
print("items[two_four] :",items[two_four])

# 可以使用切片对象改变列表原有元素
items[two_four] = [12,13]
print("items:",items)

# 删除切片元素也会跟着删除
del items[two_four]
print("items:",items)

