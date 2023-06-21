'''
主要是参数name和参数attrs的使用
以及正则的使用
find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
    Extracts a list of Tag objects that match the given
    criteria.  You can specify the name of the Tag and any
    attributes you want the Tag to have.

    The value of a key-value pair in the 'attrs' map can be a
    string, a list of strings, a regular expression object, or a
    callable that takes a string and returns whether or not the
    string matches for some custom definition of 'matches'. The
    same is true of the tag name.

Help on function find in module bs4.element:

find(self, name=None, attrs={}, recursive=True, text=None, **kwargs)
    Return only the first child of this Tag matching the given
    criteria.
'''

from bs4 import BeautifulSoup
from urllib import request
import re

# help(BeautifulSoup.find_all)
# help(BeautifulSoup.find)

def test():
    url = 'http://www.baidu.com'

    response = request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    # print(soup)
    # 搜索标签名为meta的,使用name
    tags = soup.find_all(name='meta')
    # print(tags)   # 返回一个列表
    print("tags:")
    for i in tags:
        print(i)
    print("===" *20)
    
    # 搜索标签名为meta，且标签带有属性content='IE=Edge'
    tag1 = soup.find_all(name='meta', attrs={'content': 'IE=Edge'})
    print(tag1)
    print("===" *20)    
    # 使用正则，搜索标签名开头为'me'的标签
    tag2 = soup.find_all(name=re.compile("^me"))
    for tag in tag2:
        print(tag)

if __name__ == "__main__":
    test()