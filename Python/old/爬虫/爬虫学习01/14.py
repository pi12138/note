# 打印cookie案例
from urllib import request, error, parse
from http import cookiejar

# 生成cookiejar实例
cookie = cookiejar.CookieJar()

# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 生成http管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():

    url = "http://www.renren.com/PLogin.do"
    # 登录信息
    data = {
        'email':'13193820382',
        'password':'zhou19981118'
    }

    data = parse.urlencode(data).encode()

    req = request.Request(url, data = data)

    rsp = opener.open(req)

if __name__ == "__main__":
    '''
    执行完login后会得到授权之后的cookie
    尝试打印cookie
    '''
    login()
    
    print(cookie)

    for item in cookie:
        print(item)
        # for i in dir(item):
        #     print(i)
