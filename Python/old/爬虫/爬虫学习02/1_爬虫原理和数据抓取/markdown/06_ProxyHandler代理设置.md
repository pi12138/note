# ProxyHandler处理器（代理设置）

- 使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

- 很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。
- 所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

- urllib.request中通过ProxyHandler来设置使用代理服务器，下面代码说明如何使用自定义opener来使用代理：
  - request.ProxyHandler() 的参数为一个字典,键为http/https,值为服务器地址加端口号，要禁用自动检测的代理，请传递一个空字典。

    ```python

    from urllib import request

    # 构建了两个代理Handler，一个有代理IP，一个没有代理IP
    httpproxy_handler = request.ProxyHandler({"http" : "124.88.67.81:80"})
    nullproxy_handler = request.ProxyHandler({})

    proxySwitch = True #定义一个代理开关

    # 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
    # 根据代理开关是否打开，使用不同的代理模式
    if proxySwitch:  
        opener = request.build_opener(httpproxy_handler)
    else:
        opener = request.build_opener(nullproxy_handler)

    request = request.Request("http://www.baidu.com/")

    # 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
    response = opener.open(request)

    # 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # urllib2.install_opener(opener)
    # response = urlopen(request)

    print response.read()
    ````

- 免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

## 免费短期代理网站举例

1. [西刺免费代理IP](http://www.xicidaili.com/)
2. [快代理免费代理](http://www.kuaidaili.com/free/inha/)
3. [Proxy360代理](http://www.proxy360.cn/default.aspx)
4. [全网代理IP](http://www.goubanjia.com/free/index.shtml)

- 如果代理IP足够多，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。

```python
from urllib import request
import random

proxy_list = [
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_handler = request.ProxyHandler(proxy)

opener = request.build_opener(httpproxy_handler)

request = request.Request("http://www.baidu.com/")
response = opener.open(request)
print response.read()
```

- 但是，这些免费开放代理一般会有很多人都在使用，而且代理有寿命短，速度慢，匿名度不高，HTTP/HTTPS支持不稳定等缺点（免费没好货）。
- 所以，专业爬虫工程师或爬虫公司会使用高品质的私密代理，这些代理通常需要找专门的代理供应商购买，再通过用户名/密码授权使用（舍不得孩子套不到狼）。

## 案例

- 05_设置代理池.py
- 