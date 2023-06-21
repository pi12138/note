# 使用自定义包下自定义模块

import Userpackage.module01 as u1

p1 = u1.Person('kkk', 20)

p1.introduce()

# print(Userpackage.name)		# 不能使用__init__.py 中的内容
# print(u1.name)				# 不能使用__init__.py 中的内容