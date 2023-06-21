import json

filename = 'test05.txt'

list130 = ['zyp', 'kah', 'gyj', 'gzy', 'lfs', 'zy']

dictzyp = {'name':'zyp', 'age':'20'}


with open(filename, 'w') as f:
	# 两种写入方式
	# json.dump(list130, f)
	# 使用'\n'来区分两份数据
	f.write(json.dumps(list130) + '\n')

	f.write(json.dumps(dictzyp) + '\n')


with open(filename, 'r') as f:
	data1 = json.loads(f.readline())
	print(data1)
	data2 = json.loads(f.readline())
	print(data2)
