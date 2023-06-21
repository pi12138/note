'''
如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
给 startswith() 或者 endswith() 方法：
'''

import os 

filelist = os.listdir('f:/python/oop')
for filename in filelist:
    print(filename)

match = ('.py', '.md')
new_list = [filename for filename in filelist if filename.endswith(match)]
for i in new_list:
    print(i)

print(any(name.endswith('.txt') for name in filelist))

'''
奇怪的是，这个方法中必须要输入一个元组作为参数。如果你恰巧有一个 list 或
者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型。比如：
'''
match2 = ['.py', '.md']
# new_list2 = [name.endswith(match2) for name in filelist]
# endswith first arg must be str or a tuple of str, not list
new_list2 = [name for name in filelist if name.endswith(tuple(match2))]
print(new_list2)