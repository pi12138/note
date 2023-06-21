from urllib import request, parse
from http import cookiejar

# 1. 构建一个CookieJar 对象来保持cookie
cookiejar = cookiejar.CookieJar()

# 2. 创建 cookie处理器对象
handler = request.HTTPCookieProcessor(cookiejar)

# 3. 构建opener
opener = request.build_opener(handler)

opener.addheaders = [("User_Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"),]

url = "http://www.renren.com/PLogin.do"

data = {"email":"13193820382", "password":"zhou19981118"}
data = parse.urlencode(data).encode()

req = request.Request(url, data=data, method="POST")

response = opener.open(req)

# print(response.read().decode())
# print(cookiejar)
# print(type(cookiejar))

# 查看其他人主页
response = opener.open("http://page.renren.com/601499186")

print(response.read().decode())