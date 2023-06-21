# 序列化案例
import pickle

age = 20
name = 'zyp'

# help(pickle.dump)

with open(r'./test03.txt', 'wb') as f:
	# pass
	pickle.dump(age, f)
	pickle.dump(name,f)


# 反序列化案例

# with open(r'./test03.txt', 'rb') as f:
	
# 	try:
# 		text = pickle.load(f)
# 		while text:
# 			print(text)
# 			text = pickle.load(f)
# 	except EOFError as e:
# 		print(e)
with open(r'./test03.txt', 'rb') as f:
	text1 = pickle.load(f)
	print(text1)
	text2 = pickle.load(f)
	print(text2)
	# 报错显示 EOFError
	# text3 = pickle.load(f)
	# print(text3)
