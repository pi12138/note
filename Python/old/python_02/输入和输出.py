# #str()返回一个用户易读的字符串，repr()返回一个计算器易读的字符串
# str1 = 'hello world'
# print(str(str1))
# print(repr(str1))
# #输出格式美化、
# #rjust()函数使字符串靠右对齐，在左边补齐空格，还有类似的方法ljust(),center()，
# #这些函数只会补齐空格不会添加其他内容
# #zfill()函数会在数字的左边补齐0
# #输出一个平方立方表
# for x1 in range(1,11):
# 	print(repr(x1).rjust(4), repr(x1*x1).rjust(4), end=" ")
# 	print(repr(x1*x1*x1).rjust(4))
# for x2 in range(1,11):
# 	print("{0:3d}{1:4d}{2:5d}".format(x2, x2*x2, x2*x2*x2))
# #打印乘法口诀
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("{0}*{1}={2}".format(i,j,i*j).rjust(7),end=" ")
# 	print("")

# #读写文件
# #open(filename, mode),返回一个file对象
# file1 = open('C:/Users/Administrator/Desktop/1.txt', 'r+')		#打开文件		
# # print(file1.read())											#读取文件中的所有内容
# print(file1.readline())											#读取文件中的一行
# print(file1.readline())
# print(file1.readlines())										#返回该文件的所有行
# file1.close()													#关闭文件

# #迭代读取文件所有行
# file2 = open('C:/Users/Administrator/Desktop/1.txt', 'r+')
# for line in file2:
# 	print("line:",line)
# file2.close()

# file3 = open('C:/Users/Administrator/Desktop/1.txt', 'r+')
# str1 = '55555555'
# print("write_size:",file3.write(str1))						#往文件内写内容，返回写入字符个数
# print(file3.read())
# print(file3.tell())
# file3.close()
#
# file4 = open('C:/Users/Administrator/Desktop/1.txt', 'r+')
# print(file4.readline())
# print(file4.tell())							#返回文件当前所处位置
# file4.close()

file5 = open('C:/Users/Administrator/Desktop/hello.txt', 'a+')
str_hello = 'hello,wld'
print("write_size:",file5.write(str_hello))
file5.close()
file5 = open('C:/Users/Administrator/Desktop/hello.txt', 'a+')
# print("hello.txt:",file5.readline())
# file5.seek(-2, 1)
file5.write("or")
# print("hello.txt:",file5.read())
file5.close()
file5 = open('C:/Users/Administrator/Desktop/hello.txt', 'r+')
print("hello.txt:",file5.read())
file5.close()

