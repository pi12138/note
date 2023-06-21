
# 将字符串转换为10进制数
str1 = '12345'
print(int(str1))


# 将8进制字符串转化为，10进制数
# num1 = 12345
print(int(str1, base = 8))
# help(int)

# 新建一个函数
# 函数功能为：将16进制字符串转化为10进制数
def int16(x, base = 16):
	return int(x, base)

print(int16(str1))

# 使用偏函数定义实现上述函数功能
# 将8进制字符串转化为10进制数
import functools
int8 = functools.partial(int, base = 8)
print(int8(str1))

# help(functools.partial)

help(max)