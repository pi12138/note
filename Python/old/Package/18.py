import os

# os.getcwd() 获取当前工作目录，返回当前工作目录的字符串
mydir = os.getcwd()
print(mydir)


# os.chdir() 改变当前工作目录 change directory
# help(os.chdir)
# 
# 3
# 3.
# 
os.chdir('F:/python')
print(os.getcwd()) 
os.chdir('F:/python/Package')
print(os.getcwd())


# os.listdir(path) 获取一个目录中所有的子目录和文件名称的列表
# 返回一个列表
ld1 = os.listdir()			# path = none 的情况下默认返回当前工作路径下的所有文件
ld2 = os.listdir('F:/python/Package')	# 跟上面结果一样
print(ld1)
print(ld2)


# os.makedirs(递归路径)  递归创建文件夹，无返回值
# 多个文件夹层层包围的路径就是递归路径， 例如a/b/c
# om = os.makedirs('Userpackage3')			# 在当前工作环境目录下创建一个名为Userpackage3的文件夹
# print(om)


# os.system(系统命令) 
# 打开一个shell或者终端界面
# os.system('dir')


# os.getenv('环境变量名') 获取指定的系统环境变量值
# 返回指定环境变量对应的值
# 对应还有os.putenv()
og = os.getenv('path')
print(og)


# os.exit()  推出当前程序，无返回值


# 值部分
# 	- os.curdir:current dir 当前目录
# 		- . : 代表当前目录
# 	- os.pardir:parent dir 父目录
# 		- .. : 代表父目录
# 	- os.sep：当前系统的路径分隔符
# 		- window:\
# 		- linux: /
# 	- os.linesep： 当前系统的换行符
# 		- window: \r\n
# 		- linux:\n
# 	- os.name: 当前系统名称
# 		- window: nt
# 		- linux: posix
print(os.curdir)
print(os.pardir)

print(os.sep)
print(os.linesep)
print(os.name)
