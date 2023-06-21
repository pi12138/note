'''
问题
怎样找出一个序列中出现次数最多的元素呢？

解决方案
collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的most_common() 方法直接给了你答案。
为了演示，先假设你有一个单词列表并且想找出哪个单词出现频率最高。你可以这
样做：
'''
from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

new_counter = Counter(words)

top_three = new_counter.most_common(3)
print(top_three)

# 讨论
# 作为输入，Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
# 底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：

print("eyes:",new_counter['eyes'])
print("the:",new_counter['the'])
print("look:",new_counter['look'])

# 如果你想手动增加计数，可以简单的用加法：
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    new_counter[word] += 1

print("eyes:", new_counter['eyes'])

# 或者你可以使用 update() 方法：
new_counter.update(morewords)
print("eyes:", new_counter['eyes'])
print("why:", new_counter['why'])

