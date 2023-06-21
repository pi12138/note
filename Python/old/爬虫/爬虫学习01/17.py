'''
案例存在问题，可以顺利爬取
'''

from urllib import request

import ssl

# 利用非认证上下文环境替换认证的上下文环境
# default   默认值
# unverified    adj. 未经核对的，未经证实的
ssl.create_default_context = ssl._create_unverified_context

try:
    url = 'https://www.12306.cn'

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    print(html)
except Exception as e:
    print(e)