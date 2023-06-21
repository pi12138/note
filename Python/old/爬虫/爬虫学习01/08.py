# URLError 使用

from urllib import request, error

# 访问一个不存在的网站时会报错URLError
# 访问一个存在的网站一个不存在的网页会报错HTTPError
# url = 'http://www.zypaaaa.com'
url = "http://www.sipo.gov.cn/www"

try:
	req = request.Request(url)

	rsp = request.urlopen(req)

	html = rsp.read()

	print(html)
except error.HTTPError as e:
	print("e       :", e)
	print("e.reason:", e.reason)

except error.URLError as e:
	print("e       :", e)
	print("e.reason:", e.reason)

except Exception as e:
	print("error:", e)