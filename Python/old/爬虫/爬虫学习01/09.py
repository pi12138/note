# 访问一个网址
# 更改自己的UserAgent进行伪装
from urllib import request


url = 'http://www.baidu.com'

# 1.直接设置
# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# }
# # 也可以这样
# # headers = {}
# # headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# req = request.Request(url, headers = headers)

# 2.使用函数add_header设置
# add_header(key, val) method of urllib.request.Request instance
# # help(req.add_header)

req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

response = request.urlopen(req)

html = response.read()

print(html.decode())
