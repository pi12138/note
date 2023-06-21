# URLError 使用

from urllib import request, error

url = 'http://www.1558255789.com'

try:
	req = request.Request(url)

	rsp = request.urlopen(req)

	html = rsp.read()

	print(html)
except error.URLError as e:
	print("e       :", e)
	print("e.reason:", e.reason)

except Exception as e:
	print("error:", e)