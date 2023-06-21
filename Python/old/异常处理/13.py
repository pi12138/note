# 自定义异常

class NewError(NameError):
	pass

try:
	print('1')
	print('2')
	raise NewError
	print('3')
# 捕获自定义异常，如果未使用自定义异常则会由自定义异常的父类捕获，即被NameError捕获
except NewError as e:			
	print('NewError')

except NameError as e:
	print('NameError')

except ValueError as e:
	print('ValueError')

except Exception as e:
	print('Exception')
finally:
	print('一定会被执行')