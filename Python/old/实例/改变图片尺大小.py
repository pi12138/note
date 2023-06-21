"""
该文件用于压缩图片大小
要求：
	1. 文件后缀为 '.png'
	2. 该文件和要压缩文件在同一目录下
"""
# 引入模块
from PIL import Image
import os

# 读取当前文件目录
def read_dir():
	dir_list = os.listdir()
	# print(dir_list)
	return dir_list

# 操作图片文件
def picture_handle(dir_list):
	# 定义压缩后图片大小
	size = (30, 30)
	try:
		for file in dir_list:
			# 跟据文件名判断是否为图片
			if file.endswith('.png'):
				# 打开图片
				im = Image.open(file)
				# 按指定比例压缩
				im.thumbnail(size)
				# 按原来的文件名
				im.save(file)

		return "success"
	except Exception as e:
		return "error:{0}".format(e)

if __name__ == "__main__":
	dir_list = read_dir()

	print(picture_handle(dir_list))
