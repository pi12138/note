"""
处理指定路径下的图片
可以指定处理后的尺寸
"""

from PIL import Image
import os

# import sys


def input_file_name(file_path, file_name, file_list):
	"""输入要进行操作的文件"""
	if file_name in file_list:
		handle_image()
		return "处理成功"
	else:
		return "该文件不存在！"


def read_file_path(file_path):
	"""读取文件夹,显示文件夹内容"""
	file_list = os.listdir(file_path)

	print("该目录的所有图片:")
	for file in file_list:
		if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
			print(file)

	return file_list


def handle_image():
	"""对图片进行处理"""
	try:
		# 获取压缩尺寸
		size_str = input("请输入压缩后的尺寸：")
		size = (int(size_str.split('*')[0]), int(size_str.split('*')[1]))

		# 图片处理
		im = Image.open(file_path+file_name)
		im.thumbnail(size)
		im.save(file_path+file_name)

		return "success"

	except Exception as e:
		print('error:', e)

if __name__ == "__main__":
	file_path = input("请输入文件路径:")
	file_list = read_file_path(file_path)

	file_name = input("请输入图片名:")
	result = input_file_name(file_path, file_name, file_list)

	print(result)