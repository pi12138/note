import os


if __name__ == "__main__":
	print(__name__)				# > __main__
	print(__file__)				# > 16_python中的特殊属性和方法.py
	print(os.__name__)			# > os
	print(os.path.realpath(__file__)) 		# > F:\python学习随记\py\16_python中的特殊属性和方法.py
	print(os.path.dirname(os.path.realpath(__file__))) # > F:\python学习随记\py
	print(os.path.dirname(__file__))
	print("{}/..".format(os.path.dirname(__file__)))