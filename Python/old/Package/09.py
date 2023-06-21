# __all__ 使用示例

from Userpackage2 import *

a1 = module01.Animal('Dog')

# ininit()				# 定义了__all__后，系统会默认载入__all__中内容，
						# 不会导入__init__.py文件中的其他内容