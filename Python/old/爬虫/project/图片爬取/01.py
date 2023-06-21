'''
尝试从网页抓取图片
使用urlretrieve下载????不会用
该处使用requests库中的requests.get()方法
使用urllib库不能完全爬取内容，会有4xx报错，百度推荐使用requests
可能由于抓取过多，网页不允许
抓取百度图片没有这个问题
'''
from urllib import request
import requests
from bs4 import BeautifulSoup
import re

def test(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    # req = request.Request(url, headers=headers)
    # rsp1 = request.urlopen(req)
    # html = rsp1.read()
    rsp1 = requests.get(url, headers = headers)
    html = rsp1.text
    soup = BeautifulSoup(html, 'lxml')
    
    img_url = soup.select('.photo-item__img')
    print(len(img_url))
    for img in img_url:
        if img['srcset']:
            # print(img)
            # print(img['srcset'])
            pattern = re.compile('https://images.pexels.com/photos/(.*?)/.*? 1x,')
            name = pattern.findall(img['srcset'])
            print(name)
            downurl = re.findall("(.*), https://", img['srcset'])
            
            # print(downurl)
            path = 'F:/python/爬虫/图片爬取/pexels/'
            # request.urlretrieve(downurl[0],'{0}.jpg'.format(name[0]))
            print(downurl[0])
            # req2 = request.Request(downurl[0], headers = headers)
            # rsp2 = request.urlopen(req2)
            # img_data = rsp2.read()
            rsp2 = requests.get(downurl[0], headers = headers)
            img_data = rsp2.content
            with open(path+'{0}.png'.format(name[0]), 'wb') as f:
                f.write(img_data)
                print("{0}.png已经下载".format(name[0]))
    # soup = str(soup)
    # with open(r"test01.html", 'w', encoding='utf-8') as f:
    #     f.write(soup)
    #     print("success")




if __name__ == "__main__":
    url = "https://www.pexels.com/search/snow/"
    test(url)