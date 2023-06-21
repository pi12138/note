'''
通过百度图片，爬取关键字图片
百度图片：https://image.baidu.com/
关键字：新垣结衣
'''

import requests

def BaiduImage(url):
    data = {
        'tn': 'baiduimage',
        'ipn': 'r',
        'ct': '201326592',
        'cl': '2',
        'lm': '-1',
        'st': '-1',
        'sf': '1',
        'fmq': '',
        'pv': '',
        'ic': '0',
        'nc': '1',
        'z': '',
        'se': '1',
        'showtab': '0',
        'fb': '0',
        'width': '', 
        'height':'', 
        'face': '0',
        'istype': '2',
        'ie': 'utf-8',
        'fm': 'index',
        'pos': 'history',
        'word': '新垣结衣'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    html = requests.get(url, data = data, headers = headers)
    print(html)
    # print(type(html.text))
    # print(type(html.content))
    content = html.content.decode()
    with open(data['word'] + '.html', 'w', encoding='utf-8') as f:
        f.write(content)
        print("success")

if __name__ == "__main__":
    # word = input("please a word:")

    url = "https://image.baidu.com/"
    BaiduImage(url)