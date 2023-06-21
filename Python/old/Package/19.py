from os import path as op

# os.path.abspath(path) 将路径转化为绝对路径
# absolute path
# 返回值以路径的绝对形式

# path1 = op.abspath('.')				# . 代表当前路径
# path2 = op.abspath('..')			# .. 代表父目录
# print(path1) 
# print(path2)


# os.path.basename(path) 获取路径中的文件名部分
# 返回值为文件名字符串
bn1 = op.basename('/python/Package')
print(bn1)
bn2 = op.basename('/pyhton/Package/19.py')
print(bn2)


# os.path.join(path1, path2,......)将多个路径拼接为一个路径
# 返回一个组合后的路径字符串
path1 = '\python\Package'
path2 = '19.py'
path3 = op.join(path1, path2)
print(path3)


# os.path.split(path) 将路径切割为文件夹部分和当前文件部分
# 返回路径和文件名组成的元组
path4 = op.split('/python/Package')
print(path4)

p1, p2 = op.split('/pyhton/Package/19.py')
print(p1,"  ", p2)


# os.path.isdir(file_name)  检测是否是目录
# 返回bool值
result1 = op.isdir('/python/Package')
result2 = op.isdir('/python/Package/19.py')
print(result1)
print(result2)


# os.path.exists(path)  检测文件或目录是否存在
# 返回bool
exist1 = op.exists('/python/Package/19.py')
exist2 = op.exists('/python/19.py')
print(exist1)
print(exist2)