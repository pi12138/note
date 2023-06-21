# else 使用

import sys
try:
	# print('1')
	# print('2')
	num = int(input('please a number:'))
	rst = 100 / num
	print(rst)

except Exception as e:
	print('This is except, Exception')
	print(sys.exc_info()[0])

else:
	print('This is else, No Exception!')

finally:
	print('This is finally')
