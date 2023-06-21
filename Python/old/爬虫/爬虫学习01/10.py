# 使用代理访问百度网址
from urllib import request, error

url = 'http://www.baidu.com'

# - 基本使用步骤：
# - 1.设置代理地址
proxy = {'http':'39.137.2.194:8080'}
# - 2.创建ProxyHandler,代理处理器对象
proxy_handler = request.ProxyHandler(proxy)
# - 3.创建Opener
opener = request.build_opener(proxy_handler)
# - 4.安装Opener，按照Opener之后，使用urlopen 会默认使用我们自定义的opener
# --- 构建了一个全局的Opener，之后的所有请求都可以使用urlopen()发送，也附带ProxyHandler的功能
request.install_opener(opener)

try:
	# 按照了Opener之后，下面的用法也可以写成
	# res = opener.open(url) 
    res = request.urlopen(url)
    html = res.read()
    print(html.decode())

except Exception as e:
    print(e)