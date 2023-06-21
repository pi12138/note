# 使用urllib.request获取网页内容，并打印
from urllib import request

url = "http://www.nyist.edu.cn/"

# help(request.urlopen)
# 打开一个url
# urlopen(url, data=None, timeout=<object object at 0x00000225D175B140>, *,
#  cafile=None, capath=None, cadefault=False, context=None)
#     Open the URL url, which can be either a string or a Request object.
with request.urlopen(url) as f:
	response = f.read()
	# 返回结果是bytes类型，需要解码
	# print(type(respond))
	print(response.decode())