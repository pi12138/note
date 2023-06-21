# 喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I knowyour favorite number! It's _____.”。

import json


# filename = input('please input filename:')
filename = 'filename.json'

with open(filename, 'w') as f:
	number = input('input a number:')
	json.dump(number, f)

with open(filename, 'r') as f:
	number = json.load(f)

	print("The number you entered is {0}".format(number))

