'''
这个方法仅仅在序列中元素为 hashable 的时候才管用。如果你想消除元素不可哈
希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下，就像
这样：
如果你想基于单个字段、属性或者某个更大的数据结构来消除重复元素，第二种方
案同样可以胜任。

'''

def dedupe(items, key = None):
    set1 = set()
    for item in items:
        # print("item:", item)
        # print("key:", key)
        # print("key(item):", key(item))
        val = item if key is None else key(item)
        # print(val)
        if  val not in set1:
            yield item
            set1.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(dedupe(a, key=lambda d:(d['x'],d['y']))))
print(list(dedupe(a, key=lambda d:d['x'])))