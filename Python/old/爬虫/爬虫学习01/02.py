# 利用request下载1页面
# 利用chardet检测页面编码

from urllib import request
import chardet

url = "http://www.baidu.com/"


with request.urlopen(url) as f:
	response = f.read()

	cs = chardet.detect(response)
	print(type(cs))
	print(cs)

	# 使用get取值保证不会出错
	print(response.decode(cs.get('encodeing', 'utf-8')))
	# help(cs.get)