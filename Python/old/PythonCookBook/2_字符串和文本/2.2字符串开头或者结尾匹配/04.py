'''
讨论
startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和
结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅。比如：
'''

filename = 'file.txt'

print(filename[-4:] == '.txt')

url = 'https://www.baidu.com'

print(url[:6] == 'https:' or url[:5] == 'http:' or url[:4] == 'ftp:')

'''
你可以能还想使用正则表达式去实现，比如：
'''
import re
# macth从开头开始匹配
print(re.match(r'http:|https:|ftp:', url))

'''
这种方式也行得通，但是对于简单的匹配实在是有点小材大用了，本节中的方法更
加简单并且运行会更快些。
最后提一下，当和其他操作比如普通数据聚合相结合的时候 startswith() 和
endswith() 方法是很不错的。比如，下面这个语句检查某个文件夹中是否存在指定的
文件类型：
'''
import os
print(any(name.endswith(('.py', '.md')) for name in os.listdir('f:/python/oop/')))
