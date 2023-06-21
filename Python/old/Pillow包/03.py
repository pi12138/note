"""
创建jpeg格式缩略图
"""

from __future__ import print_function
from PIL import Image
import sys

size = (128, 128)

for infile in sys.argv[1:]:
	outfile = infile.split('.')[0] + '.thumbnail'	# 生成一个16进制码的文件
	# outfile = infile.split('.')[0]+ 'new' + '.jpeg'	# 生成一张缩小图片

	if infile != outfile:
		try:
			im = Image.open(infile)
			im.thumbnail(size)
			im.save(outfile, "JPEG")

		except Exception as e:
			print('error:', e)