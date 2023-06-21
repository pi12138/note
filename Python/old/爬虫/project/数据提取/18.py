'''
css选择器
'''

from bs4 import BeautifulSoup

def test():
    with open(r"test05.html", 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')

        # 查找标签名为'div'的所有标签
        div = soup.select('div')
        print("div:")
        for i in div:
            print(i)
        print("===" * 20)

        # 查找id为'one'的标签
        id_one = soup.select('#one')
        print("id_one:")
        for i in id_one:
            print(i)
        print('===' * 20)

        # 查找类名为'first'的标签
        class_first = soup.select(".first")
        print("class_first:")
        for i in class_first:
            print(i)
        print("===" * 20)

        # 组合查找，查找类名为second的div标签
        tag1 = soup.select("div.second")
        print("tag1:", tag1)

        # 属性查找，查找带有属性"'id = 'two'"的div标签
        tag2 = soup.select('div[id="two"]')
        print("tag2:", tag2)
if __name__ == "__main__":
    test()