str1 = 'I am zyp!'
str2 = "My name is zyp!"
str3 = '''I come from China!'''

print(str1)
print(str2)
print(str3)
print("#" * 20)

str4 = 'yes,i can\'t'	#使用\转义字符
str5 = "yes,i can't"

print(str4)
print(str5)
print("*" * 20)

str6 = "frist line \nsecond line"
str7 = "frist line\
second line"
print(str6)
print(str7)

#字符串连接
str8 = 'help' + 'me'		#连接字符串
str9 = 'help ' * 5			#多次打印
print(str8)
print(str9)

print(len(str8))		#len()用于返回字符串长度
print(len(str9))			
print(str9[0:10])		#打印前10个字符
print(str9[10:])		#打印除了前10个字符的其他字符
print(str9[9:])			#打印除了前九个字符的其他字符

#python 向一个索引赋值会导致错误
# str9[0] = 'x'
# print(str9)

#允许用组合方式创建新的字符串
str10 = 'x' + str9[2:]
print(str10)

str11 = str9[:2]
str12 = str9[2:]
print(str11)
print(str12)
print(str11 + str12)

print(str9[-1])			#打印最后一个字符
print(str9[-2:-1])		#打印后两个字符
print(str9[:-2])		#打印除了后两个字符外的其他字符

