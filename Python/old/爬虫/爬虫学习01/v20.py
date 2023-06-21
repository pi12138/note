'''
爬取豆瓣剧情片前100的电影名称
'''

from urllib import request
import json

def getName():
    # 前20部的url
    # url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
    # 更改上述url，可以获得前100部的url
    for i in range(0, 100, 20):
        url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={0}&limit=20'.format(i)
        # print(i)
        try:
            with request.urlopen(url) as f:
                html = f.read().decode()

                html = json.loads(html)

                for item in html:
                    print(item['rank'], '---', item['title'])
                    # for name in item['title']:
                    #     print(name)
        except Exception as e:
            print("error:", e)


if __name__ == '__main__':
    getName()