'''
尝试抓取百度图片
使用二进制方式下载
'''

from urllib import request
import re

# help(re.findall)

def Download(url):
    rsp = request.urlopen(url)
    html = rsp.read()
    html = html.decode()
    # with open(r'test02.html', 'w', encoding = 'utf-8') as f:
    #     f.write(html)
    #     print("success")
    pattern = '"middleURL":"(.*?)"'
    url_list = re.findall(pattern, html)
    # print(url_list)
    j = 1    
    for i in url_list:
        print(i)
        rsp2 = request.urlopen(i)
        img = rsp2.read()
        with open(r'{0}.jpg'.format(j), 'wb') as f:
            f.write(img)
            print("{0}.jpg下载成功".format(j))
            j = j + 1
    # url_set = set(url_list)
    # print(len(url_set))


if __name__ == "__main__":
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1526269427171_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8"

    Download(url)