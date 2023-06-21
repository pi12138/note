"""
爬取url网页上的win dos命令行内容
存储到桌面文件
"""



import requests
from bs4 import BeautifulSoup

url = "https://blog.csdn.net/ternence_hsu/article/details/70739002"

html = requests.get(url)

soup = BeautifulSoup(html.text, 'lxml')
# style="font-family:'Courier New'
title = soup.select('''h1[class="title-article"]''')
title = title[0].text
text = soup.select('''span[style="font-family:'Courier New';"]''')

print(title)
print(len(text))

with open(title + '.txt', 'w', encoding='utf-8') as f:
    for i in text:
    # print(i.text)
        f.write(str(i.text)+'\n')
    
    print(title)