from urllib import request
from bs4 import BeautifulSoup

def test():
    # url = 'http://www.baidu.com'

    # headers = {

    # }

    # response = request.urlopen(url)
    with open(r'test04.html', 'r', encoding = 'utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')

        print(type(html))
        print(type(soup))

        print("===" * 10)

        print('div_content:',soup.div)
        print('div_type:', type(soup.div))
        print('div.h1.string:', soup.div.h1.string)
        print('h1.string:', type(soup.h1.string))
        print("===" * 10)

        print('p.string:', soup.p.string)
        print(type(soup.p.string))

        
if __name__ == "__main__":
    test()
