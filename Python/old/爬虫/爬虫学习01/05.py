# 可以进行英译汉的功能
from urllib import request, parse
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

res = request.urlopen(url, data = data)

json_data = res.read()
json_data = json_data.decode()
json_data = json.loads(json_data)
print(type(json_data))

# print(json_data)

for i in json_data['data']:
	# print(i)
	print(i['k'], '---', i['v'])
