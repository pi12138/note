#!/usr/bin/python3
#-*-coding:utf-8 -*-
'a test module'

import sys

def test():
	args = sys.argv
	print('args[0]:',args[0])
	if len(args) == 1:
		print('hello world!')
	elif len(args) == 2:
		print('hello {0}'.format(args[1]))
	else:
		print('Too many arguments')
if __name__ == '__main__':
	test()