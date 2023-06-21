'''
使用requests库
对比一下和urllib库的去呗
r = requests.get(url)
r.headers
#http响应内容的头部内容，来返回get请求获得网页的头部信息。
r.status_code
#http请求的返回状态，200表示连接成功，404表示连接失败
r.text
#http响应内容的字符串形式，url对应的页面内容
r.encoding
#从HTTP header中猜测的响应内容编码方式
r.apparent_encoding
#从内容分析出的响应内容的编码方式（备选编码方式）
r.content
#HTTP响应内容的二进制形式

'''

import requests
from urllib import request

# help(requests)

url = 'http://www.baidu.com'
response1 = requests.get(url)
# help(requests.get)
# print(response1.text)
print(type(response1.text))
print(response1)

response2 = requests.request('get', url)
# print(response2.text)
print(type(response2.text))


response3 = request.urlopen(url)
html = response3.read()
# print(html)
print(type(html))
# print(html.decode())
print(type(html.decode()))