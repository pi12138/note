'''

'''

from bs4 import BeautifulSoup
from urllib import request

def test():
    with open(r'test04.html', 'r', encoding = 'utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

        # contents打印子节点会连内容一起输出
        print("html的直接子节点：\n", soup.html.contents)
        # 返回一个list_iterator
        print("html的直接子节点：", soup.html.children)
        for i in soup.html.children:
            print(i)
        # 返回一个generator
        print("html的所有子孙节点：\n", soup.html.descendants)
        for i in soup.html.descendants:
            print(i)

        # string
        print('string' + '=' * 50)
        print("标签只有一个NavigableString：", soup.p.string)
        print("标签内有多个NavigableString：", soup.div.string)
        # strings
        print('strings' + '=' * 50)
        print("标签只有一个NavigableString：", soup.p.string)
        print("标签内有多个NavigableString：", soup.div.strings)
        for i in soup.p.strings:
            print(i)
        for i in soup.div.strings:
            print(i)
        # stripped_strings
        print('stripped_strings' + '=' * 50)
        print("soup.div.strings:", soup.div.strings)
        print("soup.div.stripped_strings:", soup.div.stripped_strings)
        for i in soup.div.strings:
            print(i)

        for i in soup.div.stripped_strings:
            print(i)

        

if __name__ == "__main__":
    
    test()