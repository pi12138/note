"""
从图片1上剪切一块区域，粘贴到图片2上
"""
from __future__ import print_function
from PIL import Image

box = (100, 100, 400, 400)		# 左上右下

im1 = Image.open('1.jpeg')
im2 = Image.open('2.jpeg')

region = im1.crop(box)

# print(region)
region.show()
# im1.show()

region = region.transpose(Image.ROTATE_180)
im2.paste(region, box)
im2.show()