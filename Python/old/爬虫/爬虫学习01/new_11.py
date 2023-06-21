# http://www.renren.com/968602505/profile

# 不使用cookie登录,无法登录到自己想要的网页
# 会自动跳转到人人网登录页面
from urllib import request, error

url = 'http://www.renren.com/968602505/profile'

try:
    response = request.urlopen(url)

    html = response.read()

    print(type(html))
    html = html.decode()
    print(type(html))
    # print(html)
    with open('new_11.html', 'w') as f:
        f.write(html)

except error.URLError as e:
    print("URLError:", e)

except Exception as e:
    print("Exception:", e)