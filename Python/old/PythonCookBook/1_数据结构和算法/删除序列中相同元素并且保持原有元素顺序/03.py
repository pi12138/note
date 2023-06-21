'''
讨论
如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。比如：

然而，这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。而上面的
方法可以避免这种情况。
在本节中我们使用了生成器函数让我们的函数更加通用，不仅仅是局限于列表处
理。比如，如果如果你想读取一个文件，消除重复行，你可以很容易像这样做：
'''

a = [1, 5, 2, 1, 9, 1, 5, 10]

set_a = set(a)
print(set_a)

def dedupe(f):
    set_f = set()
    for line in f:
        # print(line)
        if line not in set_f:
            # yield line
            set_f.add(line)
    print(set_f)
    # print(str(set_f))
    with open('remove'+f.name, 'w') as new_f:
        new_f.writelines(set_f)


with open('v03.txt', 'r') as f:
    print(f.name)
    print(type(f.name))
    dedupe(f)