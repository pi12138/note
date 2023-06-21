"""
通过查看网页源代码提交表单
豆瓣网"https://www.douban.com/"
"""
import requests

url = 'https://www.douban.com/accounts/login'

params = {
	'source': 'index_nav',
	'form_email': '2059233910@qq.com',
	'form_password': 'zhou19981118',

}

html = requests.post(url, params)
# print(html.text)
with open(r'豆瓣个人主页.html', 'w', encoding='utf-8') as f:
	f.write(html.text)
	print('success')