'''
自动使用cookie进入人人网个人主页
可以对比13.py
相比urllib库更加好使
'''

import requests
import json

def login():
    url = "http://www.renren.com/PLogin.do"

    data = {
        'email': '13193820382',
        'password': 'zhou19981118'
    }

    # 先创建session对象
    ss = requests.session()

    # 传入post
    ss.post(url, data = data)

    rsp = ss.get('http://www.renren.com/968608156/profile')

    print(type(rsp.content))

    html_data = rsp.content.decode()
    with open(r'26.html', 'w', encoding='utf-8') as f:
        f.write(html_data)
        print("write success")

if __name__ == "__main__":
    login()
    