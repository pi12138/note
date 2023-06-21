# QQ号验证
import re

QQ = input("请输入qq账号：")
password = input("请输入密码：")

# print(QQ)
# print(re.match(r'[0-9]{5,12}', QQ)))
# 此处[]内两个字符间使用'-'分割，{}内两个数字使用','分割
if re.match(r'[0-9]{5,12}', QQ):
	print("账号输入正确")
	if re.match(r'[0-9a-zA-Z_]{10,16}', password):
		print("密码输入正确")
	else:
		print("密码错误")
else:
	print("账号错误")

