'''
requests使用代理
与10.py对比
'''

import requests
import json


url = 'http://www.baidu.com'

proxies = {
    'http':'39.137.2.194:8080'
}

rsp = requests.get(url, proxies = proxies)

print(rsp.text)