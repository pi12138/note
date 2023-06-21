'''
查看beautifulsoup对象
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

    print(soup.name)    # [document]
    print(soup.attrs)   # {}
    # print(soup.text)  # 网页内容
    # print(soup.string)    # None
    # print(soup.strings)   # generator

if __name__ == "__main__":
    test()
