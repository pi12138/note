# 异常处理简单案例

import sys
# 
try:
	num = int(input("请输入数:"))
	rst = 100/num
	print("100/num = {0}".format(rst))

except ZeroDivisionError as zde:
	print(zde)
	print(type(zde))
	exit()
# except:														
# 	print("输入内容存在错误")

# 	# priznt(sys.exc_info()[0])
# 	raise
# 	exit()
