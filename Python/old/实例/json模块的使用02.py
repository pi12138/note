# 记记住住喜喜欢欢的的数数字字 ：将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，
# 就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作

import json 

filename = 'filename.json'

try:
	with open(filename, 'r') as f:
		number = json.load(f)
		
		print('The number you entered is {0}'.format(number))

except Exception:
	number = int(input('please enter a number:'))

	with open(filename, 'w') as f:
		
		json.dump(number, f)