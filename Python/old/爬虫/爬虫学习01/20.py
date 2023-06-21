'''
爬取豆瓣电影数据
了解ajax的基本爬取方式
'''

from urllib import request
import json

def getInfo():
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

    with request.urlopen(url) as f:
        html = f.read().decode()
        # html = list(html)
        print(type(html))   # 直接爬取下来后是str格式
        # print(html)
        # for i in html:
        #     print(i)
        html = json.loads(html) # 转为json格式
        print(type(html))   # 此时显示是list
        for item in html:   # 遍历list
            # print(item)
            # print(type(item))     # list里装的是dict
            for k, v in item.items():   # 遍历dict
                print(k, '---', v)

if __name__ == '__main__':
    getInfo()


