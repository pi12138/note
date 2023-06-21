from urllib import request
import random

# 1. 设置代理池
proxy_pool = [
    {"HTTP":"113.121.152.98:9999"},
    {"HTTP":"222.189.144.4:9999"},
    {"HTTP":"163.125.234.120:8118"},
    {"HTTP":"122.234.24.60:9000"},
    {"HTTP":"59.62.166.16:9999"},
    {"HTTP":"111.177.162.81:9999"},
]
proxy = random.choice(proxy_pool)

# 2. 创建 处理器对象
proxy_handler = request.ProxyHandler(proxy)

# 3. 构建 opener对象
opener = request.build_opener(proxy_handler)

# 4. 发送请求
response = opener.open("http://www.baidu.com/")

html = response.read().decode()

print(html)


