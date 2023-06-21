# raise 手动引发异常
# raise error_type

try:
	print('12345')
	print('hello world')

	raise ValueError
	print('上面手动引发异常')

except NameError as e:
	print("NameError")

except ValueError as e:
	print("ValueError")

except Exception as e:
	print("Exception")

finally:
	print("finally")