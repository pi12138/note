# 导入自定义模块中的指定内容

# 导入自定义模块Package01中的Student类
from Package01 import Student

stu = Student()			# 导入指定内容，使用时不用在加上模块名
stu.introduce()

# sayhello()			# 未导入该内容，不能使用