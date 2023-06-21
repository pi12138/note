# 使用序列化保存一些结构化的数据
import pickle

list130 = ['zyp', 'kah', 'gyj', 'gzy', 'lfs', 'zy']

dictzyp = {'name':'zyp', 'age':'20', 'address':'信阳'}

with open(r'./test04.txt', 'wb') as f:
	pickle.dump(list130, f)
	pickle.dump(dictzyp, f)

with open(r'./test04.txt', 'rb') as f:
	data = pickle.load(f)
	# while data:
	print(data)
	data = pickle.load(f)
	print(data)

# help(pickle.load)


# help(pickle.loads)