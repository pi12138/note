import shelve

# # shelve 只读打开	？？？？？
# # 为什么还可以写入数据 ？？？
# # 

# shv = shelve.open(r'test01.db', flag = 'r')

# try:
# 	k1 = shv['name']
# 	print(k1)

# 	shv['hobby'] = 'play games'
# 	print(shv['hobby'])
# # except Exception as e:
# 	# print(e)

# finally:
# 	shv.close()

shv = shelve.open(r'test01.db')
try:
	key_hobby = shv['hobby']
	print(key_hobby)
	shv['hobby'] = 'do sports'

except Exception as e:
	print(e)

finally:
	shv.close()

shv = shelve.open(r'test01.db')
try:
	key_hobby = shv['hobby']
	print(key_hobby)
	# shv['hobby'] = 'do sports'

except Exception as e:
	print(e)

finally:
	shv.close()
