import zipfile

# zipfile.ZipFile(file)
# 创建一个ZipFile对象，表示一个zip文件
# 参数file表示文件路径或者文件对象
# help(zipfile.ZipFile)
zf = zipfile.ZipFile('./Userpackage.zip')


# ZipFile.getinfo(name)
# 获取zip文档内的指定文件信息。
# 返回一个zipfile.ZipInfo对象，它包括文件的详细信息
result1 = zf.getinfo('copy20.txt')
result2 = zf.getinfo('copy20.py')
print(result1)
print(result2)
# help(zf.getinfo)


# ZipFile.namelist()
# 获取zip文档内所有文件的名称列表
nl1 = zf.namelist()
print(nl1)


# ZipFile.extractall(path)
# 解压zip文档中所有文件到当前目录
result3 = zf.extractall('./Userpackage2')
print(result3)