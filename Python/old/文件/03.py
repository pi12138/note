# 打开文件后从第五个字节开始读取


with open(r'F:/python/文件/test02.txt', 'r') as f:
	# 文件打开后读写指针在0处，即文件开头
	# seek移动单位是字节
	# 汉字一个占两个字节
	f.seek(6, 0)
	strChar = f.read()
	print(strChar)