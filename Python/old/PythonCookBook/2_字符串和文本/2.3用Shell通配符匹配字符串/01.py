'''
问题
你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文本字符串

解决方案
fnmatch 模块提供了两个函数——fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配。用法如下：
'''
from fnmatch import fnmatch,fnmatchcase
# *       matches everything
# ?       matches any single character
# [seq]   matches any character in seq
# [!seq]  matches any char not in seq
print(fnmatch('file.py', '*.py'))
print(fnmatch('file.py', '?ile.py'))
print(fnmatch('file100.py', 'file[0-9]*'))

file_list = ['file01.py','file02.py','file.txt','file.md','file03.py',]
py_list = [name for name in file_list if fnmatch(name, 'file*.py')]
print(py_list)