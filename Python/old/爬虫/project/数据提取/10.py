'''
格式化函数prettify()
'''

from bs4 import BeautifulSoup
from urllib import request

def test(url):
    response = request.urlopen(url)
    content = response.read()
    
    print(type(content))

    soup = BeautifulSoup(content, 'lxml')
    # print(type(soup))
    content = soup.prettify()
    print(content)

if __name__ == "__main__":
    url = 'http://www.baidu.com'
    test(url)
