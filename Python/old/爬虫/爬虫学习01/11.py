# 不使用cookie登录
from urllib import request, error

url = 'http://mail.qq.com/cgi-bin/frame_html?sid=sx5G189LDO0PYDxn&r=b9e5e5ee251de2d7e6655b5a7fda3b83'


try:
    response = request.urlopen(url)

    html = response.read()

    print(type(html))
    html = html.decode('gbk')
    print(type(html))
    # print(html)
    with open('11.html', 'w') as f:
        f.write(html)

except error.URLError as e:
    print("URLError:", e)

except Exception as e:
    print("Exception:", e)