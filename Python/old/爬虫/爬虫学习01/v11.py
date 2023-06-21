# 爬取qq邮箱登录页面与11.html对比
from urllib import request, error

url = 'http://mail.qq.com'

try:
    response = request.urlopen(url)

    html = response.read()

    html = html.decode('gbk')

    with open('v11.html', 'w') as f:
        f.write(html)

except Exception as e:
    print("error:", e)


