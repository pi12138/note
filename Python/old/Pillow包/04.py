"""
识别图像文件
"""
from __future__ import print_function
from PIL import Image
import sys

for infile in sys.argv[1:]:
	try:
		with Image.open(infile) as im:
			print("文件名： ", infile)
			print("文件格式：", im.format)
			print("文件尺寸：", im.size)
			print("文件模式：", im.mode)
	except Exception as e:
		print("error:", e)