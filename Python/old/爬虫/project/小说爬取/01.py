'''
练习爬取小说单章节内容
'''
import requests
from bs4 import BeautifulSoup
import re


def chapter(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    rsp = requests.get(url, headers = headers)

    str1 = rsp.text
    soup = BeautifulSoup(str1, 'lxml')
    # str2 = str(soup.select('.showtxt'))
    # str3 = str2.replace('<br/>', "")
    str2 = soup.find_all(name = 'div', class_ = 'showtxt')
    str2 = str(str2)
    str3 = str2.replace("<br/>", '')
    # 通过指定分隔符对字符串进行切片
    str4 = str3.split()
    
    title = soup.h1.string
    print(title)
    # print(type(str2))
    # print(str2)
    # print(type(str3))
    with open(title+'.txt', 'w', encoding = 'utf-8') as f:
        for i in str4:
            # print(i)
            f.writelines(i)
            f.writelines('\n')
        # f.write(str4)
        print("success")

    # print(type(rsp.text))
   

if __name__ == "__main__":
    url = 'https://www.biqukan.com/0_790/15948251.html'
    chapter(url)
