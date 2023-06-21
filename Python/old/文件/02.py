# help(with)

# 按行读取
with open(r'F:/python/文件/test01.txt', 'r') as f:
	# 按行读取内容
	strline = f.readline()

	# while 循环保证可以将文件读取知道结束
	while strline:
		print(strline)
		strline = f.readline()

	print('frist' * 10)

# 全部读取
# read([size]) 按字符读取文件内容，没有输入size默认读取全部
with open(r'F:/python/文件/test01.txt', 'r') as f:
	text = f.read()

	print(text)
	print('second' * 10)

# list能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r'F:/python/文件/test01.txt', 'r') as f:
	txt_list = list(f)
	# print(txt_list)
	for i in txt_list:
		print(i)
	print('third' * 10)
# help(list)

# 使用read()每次读取一个字符，依次读完
with open(r"F:/python/文件/test01.txt", 'r') as f:
	strChar = f.read(1)
	print(strChar, end = '')
	while strChar:
		strChar = f.read(1)
		print(strChar, end = '')	