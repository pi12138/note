# Email验证
# 
import re

email = input("输入邮箱：")

if re.match(r'^[0-9]{5,12}\@(qq|sina)\.com$', email):
	print(email)

else:
	print('false')