# ???

# 可以进行英译汉的功能
from urllib import request, parse, error
import json

url = 'https://fanyi.baidu.com/sug'
kw = input("please a kw:")
# kw需要进行url编码
# kw = parse.urlencode(kw)

data = {
	'kw':kw
}

headers = {
	'Content-Length':len(data)
}

data = parse.urlencode(data)

data = data.encode()
# 构建一个Request实例
# req = request.Request(url = url, data = data)
try:
	req = request.Request(url = url, data = data, headers = headers)
# 此处headers使用没有问题，但是传入headers无法爬出数据？？？？


# 因为已经构建了一个Request实例，则对所有的请求信息都可以封装在Request实例中
# urlopen直接打开Reques实例即可
	res = request.urlopen(req)

	json_data = res.read()
	json_data = json_data.decode()
	json_data = json.loads(json_data)
	print(type(json_data))

	print(json_data)

	for i in json_data['data']:
	# print(i)
		print(i['k'], '---', i['v'])

except error.URLError as e:
	print("error       :", e)
	print("error.reason:", e.reason)

except Exception as e:
	print("error:", e)
