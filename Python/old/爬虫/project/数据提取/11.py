'''
使用soup.tag_name来提取标签内容
查看soup.tag_name 属于什么对象
使用soup.tag_name 来查找标签，只能查找到同名标签中的第一个
查看标签name,attrs,text
name可以查看标签名，返回一个str类型
attrs可以查看标签属性，返回一个dict类型
text可以查看标签文本内容，返回一个str
'''

from urllib import request
from bs4 import BeautifulSoup

def test():
    url = 'http://www.baidu.com'

    # headers = {

    # }

    response = request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    print(type(html))
    print(type(soup))

    # 查看head标签
    print(soup.head)
    print(type(soup.head))
    print("++++" * 20)
    # 查看meta标签
    print(soup.meta)
    print(type(soup.meta))
    print("++++" * 20)
    # 查看link标签
    print(soup.link)
    print(type(soup.link))
    print("++++" * 20)
    # 查看标签name和attrs
    print('text:', soup.link.text)
    print(type(soup.link.text))
    print(soup.link.name)
    print(type(soup.link.name))
    print(soup.link.attrs)
    print(soup.link.attrs['type'])  # 查看标签指定属性内容
    soup.link.attrs['type'] = '内容也可以修改'  # 属性内容也可以修改
    print(soup.link)
    print(type(soup.link.attrs))
    print("++++" * 20)
    # 查看title标签内容
    print(soup.title)
    print(soup.title.text)
    print(soup.title.name)
    print(soup.title.attrs)

if __name__ == "__main__":
    test()

