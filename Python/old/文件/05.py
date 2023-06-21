# 1.向文件追加一行
#

with open(r'F:/python/文件/test02.txt', 'a') as f:
	# position = f.tell()
	# print(position)
	str1 = '\n这是一个用write函数写入文件的内容'
	f.write(str1)

	# 此时光标在文件尾，需要移动到文件头才能读取文件内容
	# f.seek(0, 0)

	# 文件是以'a' 的方式打开只能用于追加，不能读取
	# text = f.read()
	# print(text)

with open(r'F:/python/文件/test02.txt', 'r') as f:
	text = f.read()
	print(text)