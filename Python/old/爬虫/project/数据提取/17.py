'''
参数text和参数**kwargs的使用
'''

from bs4 import BeautifulSoup

def test():
    with open(r'test05.html', 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')

        # 使用**kwargs，查找"id = 'one'"的标签
        tag1 = soup.find_all(id='two')
        print(tag1)        
        # 返回的内容为查找的text而不是标签
        tag2 = soup.find_all(text = '这是第一个')
        print(tag2)

if __name__ == "__main__":
    test()