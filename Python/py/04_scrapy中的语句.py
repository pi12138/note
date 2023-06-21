dict1 = {
	"path": "xxxxxxxx"
}
dict2 = {
	'path': 'aaaaaaa'
}
dict3 = {
	'path': 'bbbbbbb'
}

result = [(True, dict1), (False, dict2), (True, dict3)]

# 这是一个列表生成式
"""
理解：是将results的值分别给x,ok,如果ok的值为True,那么就取x['path']最后形成一个一个list
"""
path = [x['path'] for ok, x in result if ok]

print(path)		# > ['xxxxxxxx', 'bbbbbbb']


# 拆开写
for ok, x in result:
	if ok:
		print(x['path'])
# > xxxxxxxx
# > bbbbbbb

