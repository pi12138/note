'''
练习爬取小说单章节内容
使用get_text()处理多余标签和其他内容更好
但是内容不会自动换行
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
    str2 = soup.findAll('div', {'class': 'showtxt'})
  
    # print(type(str2))
    
    title = soup.h1.string
    print(title)
    # print(type(str2))
    # print(str2)
    # print(type(str3))
    with open(title+'.txt', 'w', encoding = 'utf-8') as f:
        for text in str2:
            # print(text.get_text())
            f.writelines(text.get_text() + '\n')
            # f.writelines('\n')
        # f.write(str2)
        print("success")

    # print(type(rsp.text))
   

if __name__ == "__main__":
    url = 'https://www.biqukan.com/0_790/15951380.html'
    chapter(url)
