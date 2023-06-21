'''
这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很
有用的。比如，假设你有一个街道地址的列表数据：
'''

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

'''
你可以像这样写列表推导：
'''

from fnmatch import fnmatchcase

ST_addresses = [name for name in addresses if fnmatchcase(name, '*ST')]
AVE_addresses = [name for name in addresses if fnmatchcase(name, '*AVE')]

print(ST_addresses)
print(AVE_addresses)

'''
讨论
fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。如果在
数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
如果你的代码需要做文件名的匹配，最好使用 glob 模块。参考 5.13 小节。
'''