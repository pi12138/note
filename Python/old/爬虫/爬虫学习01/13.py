# 使用cookiejar自动登录

from urllib import request, parse
from http import cookiejar

# 创建cookiejar实例
cookie = cookiejar.CookieJar()

# 创建cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户账号和密码，用来获取登录cookie凭证
    :return:
    ''' 
    url = "http://www.renren.com/PLogin.do"

    data = {
        'email':'13193820382',
        'password':'zhou19981118'
    }
    # 对上传数据进行编码
    data = parse.urlencode(data).encode('utf-8')
    # 传入账号密码
    # 得到返回
    req = request.Request(url, data = data)

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'http://www.renren.com/968608156/profile'

    # 如果已经执行了login()函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)
    
    html = rsp.read().decode('utf-8')

    with open(r'13.html', 'w', encoding='utf-8 ') as f:
        f.write(html)

if __name__ == "__main__":
    login()

    getHomePage()

