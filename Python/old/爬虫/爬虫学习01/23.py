'''
使用requests.post
百度翻译英译汉
'''

import requests
import json

def baidufanyi(kw):
    url = "https://fanyi.baidu.com/sug"

    data = {
        'kw': kw
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    # requests.post 的好处是data不用编码
    response = requests.post(url, data = data, headers = headers)

    # 下面两种均为解码，无法看的懂内容
    # print(response.text)
    # print(response.content)

    # print(response.json())        # 返回人类可以读的懂的内容
    # 对返回内容稍微处理
    # print(type(response.json()))
    data = response.json()
    # print(type(data['data']))
    for i in data['data']:
        print(i['k'], '---', i['v'])

if __name__ == "__main__":
    kw = input("please a kw:")
    baidufanyi(kw)