'''
可以读取磁盘文件或者爬虫文件
'''

from urllib import request

def read_data(name):
    match = ('http:', 'https:', 'ftp:')
    if name.startswith(match):
        return request.urlopen(name).read()
    else:
        with open(name, 'r', encoding='utf-8') as f:
            return f.read()

# 读取文件
print(read_data('f:/python/oop/01.py'))

# 爬取网页
print(read_data('http://www.baidu.com').decode())
