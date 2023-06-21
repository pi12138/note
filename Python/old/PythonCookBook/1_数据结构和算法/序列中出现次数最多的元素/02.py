'''
Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比如：

毫无疑问，Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
'''

from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)

print("a:", a)
print("b:", b)

c = a + b
print("c:", c)

d = a - b
print("d:", d)
