"""
python实现字符串加密的几种方式
	1. md5
	2. sha1
"""
"""
hash.update（数据）
使用类似字节的对象更新哈希对象。重复调用相当于单个调用，并且所有参数都连接在一起：相当于。m.update(a); m.update(b)m.update(a+b)

在3.1版中更改：发布Python GIL以允许其他线程运行，而在使用OpenSSL提供的哈希算法时，对大于2047字节的数据进行哈希更新。

hash.digest（）
返回update()到目前为止传递给方法的数据的摘要。这是一个大小的字节对象digest_size，可能包含0到255范围内的整个字节。

hash.hexdigest（）
就像digest()除了摘要作为双倍长度的字符串对象返回，只包含十六进制数字。这可用于在电子邮件或其他非二进制环境中安全地交换值。
"""

import hashlib

def encryption_md5(str):
	# 创建md5对象
	md5 = hashlib.md5()

	# 更新哈希对象，参数要为 bytes 类型
	md5.update(str.encode())

	# 返回加密结果，为bytes 类型
	new_str = md5.digest()
	# new_str = md5.hexdigest()		# 可以被解密

	# new_str 无法decode()解码
	print(new_str)
	print(type(new_str))
	# 加密后的二进制字符长度为16
	print(len(new_str))


def encryption_sha1(str):
	# 创建哈希对象
	sha1 = hashlib.sha1()

	sha1.update(str.encode())

	new_str = sha1.hexdigest()

	# new_str 无法decode()解码
	print(new_str)
	print(type(new_str))
	# 加密后的二进制字符长度为16
	print(len(new_str))

if __name__ == "__main__":

	str = 'zhou19981118'

	encryption_md5(str)
	encryption_sha1(str)