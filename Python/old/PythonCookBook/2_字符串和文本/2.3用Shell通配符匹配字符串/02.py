'''
fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来匹配模式。比如：
>>> # On OS X (Mac)
>>> fnmatch('foo.txt', '*.TXT')
False
>>> # On Windows
>>> fnmatch('foo.txt', '*.TXT')
True
如果你对这个区别很在意，可以使用 fnmatchcase() 来代替。它完全使用你的模
式大小写匹配。比如：
'''

from fnmatch import fnmatchcase

print(fnmatchcase('file.txt', '*.TXT'))

