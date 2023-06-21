'''
在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有
一个列表，你可以很容易的将它分割成前后两部分：

如果你够聪明的话还能用这种分割语法去巧妙的实现递归算法
'''

item = [1, 2, 3, 4, 5]

head,*tail = item
print("head:",head)
print("tail:",tail)


def digui(item):
    head,*tail = item
    return head+sum(tail) if tail else head

print(digui(item))