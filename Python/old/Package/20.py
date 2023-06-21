import shutil
import os

# shutil.copy(来源路径， 目标路径)
# 返回值为目标路径
# 拷贝同时可以给目标重新命名 
# result1 = shutil.copy("/python/Package/20.py", "/python/Package/Userpackage/copy20.py")
# print(result1)


# shutil.copy2(来源路径，目标路径) 
# 同样是复制文件，保留元数据（文件信息）
# 返回目标路径
# copy和copy2 的唯一区别在于copy2复制文件时尽量保留元数据


# shutil.copyfile(源路径， 目标路径)  将文件中的内容复制到另一个文件当中
# 返回值为目标路径
# help(shutil.copyfile)
# result2 = shutil.copyfile('20.py', 'copy20.txt')
# print(result2)
# print(os.getcwd())


# shutil.move(源路径，目标路径)
# 返回目标路径
# result3 = shutil.move('./copy20.txt', './Userpackage')
# print(result3)


# 归档和压缩
# 	- 归档:把多个文件或者文件夹合并到一个文件当中
# 	- 压缩：用算法把多个文件或者文件夹无损或者有损的合并到一个文件中
# 
#  shutil.make_archive("归档后的目录与文件名", "后缀", "归档需要的文件夹")
#  返回值为归档之后的地址
# result4 = shutil.make_archive('./Userpackage', 'zip', 'Userpackage' )
# print(result4) 


# shutil.unpack_archive('归档文件地址'，'解包之后地址')
# 返回值为None
# result5 = shutil.unpack_archive('./Userpackage.zip', './Userpackage/Userpackage')
# print(result5)
# help(shutil.unpack_archive)