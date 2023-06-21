'''

问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？
解决方案

如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解
决这个问题。比如：
'''

def dedupe(items):
    set1 = set()

    for item in items:
        if item not in set1:
            yield item
            set1.add(item)
    
a = [1,2,3,4,5,3,2,1]
print(list(dedupe(a)))

