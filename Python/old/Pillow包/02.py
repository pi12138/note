"""
改变文件格式，为.jpg结尾
"""
from __future__ import print_function
from PIL import Image
import sys

# sys.argv可以实现从程序外部传入参数，列表中第一个参数是文件本身，即02.py
for infile in sys.argv[1:]:
	f, f_e = infile.split('.')
	outfile = f + '.jpg'

	if outfile != infile:
		try:
			Image.open(infile).save(outfile)
		except Exception as e:
			print("error:", e)
