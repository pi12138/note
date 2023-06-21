'''
查看NavigableString对象，和tag对象的不同
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

 
    # 查看link标签
    print(soup.link)
    print(type(soup.link))
    print("++++" * 20)
    # 查看标签name和attrs
    # print('text:', soup.link.text)
    # print(type(soup.link.text))
    # print(soup.link.name)
    # print(type(soup.link.name))
    # print(soup.link.attrs)
    # print(soup.link.attrs['type'])  # 查看标签指定属性内容
    # soup.link.attrs['type'] = '内容也可以修改'  # 属性内容也可以修改
    # print(soup.link)
    # print(type(soup.link.attrs))
    # print("++++" * 20)
    # 查看title标签内容
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    print(type(soup.title.string))  # 打印内容为navigablestring类型
    # print(soup.title.name)
    # print(soup.title.attrs)

if __name__ == "__main__":
    test()
