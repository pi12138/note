# Cookie

- Cookie 是指某些网站服务器为了辨别用户身份和进行Session跟踪，而储存在用户浏览器上的文本文件，Cookie可以保持登录信息到用户下次与服务器的会话。

## Cookie原理

- HTTP是无状态的面向连接的协议, 为了保持连接状态, 引入了Cookie机制 Cookie是http消息头中的一种属性，包括：

- Cookie名字（Name）
- Cookie的值（Value）
- Cookie的过期时间（Expires/Max-Age）
- Cookie作用路径（Path）
- Cookie所在域名（Domain），
- 使用Cookie进行安全连接（Secure）。

- 前两个参数是Cookie应用的必要条件，另外，还包括Cookie大小（Size，不同浏览器对Cookie个数及大小限制是有差异的）。
- Cookie由变量名和值组成，根据 Netscape公司的规定，Cookie格式如下：
`Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE`

## Cookie应用

- Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续。

## 获取一个有登录信息的Cookie模拟登陆

```python
from urllib import request

# 1. 构建一个已经登录过的用户的headers信息
headers = {
    "Host":"www.renren.com",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",

    # 便于终端阅读，表示不支持压缩文件
    # Accept-Encoding: gzip, deflate, sdch,

    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "anonymid=ixrna3fysufnwv; depovince=GW; _r01_=1; JSESSIONID=abcmaDhEdqIlM7riy5iMv; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484060607173; jebecookies=26fb58d1-cbe7-4fc3-a4ad-592233d1b42e|||||; ick_login=1f2b895d-34c7-4a1d-afb7-d84666fad409; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=99e54330ba9f910b02e6b08058f780479; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=214ca9a28f70ca6aa0801404dda4f6789; societyguester=214ca9a28f70ca6aa0801404dda4f6789; id=327550029; xnsid=745033c5; ver=7.0; loginfrom=syshome"
}

# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
req = request.Request("http://www.renren.com/", headers = headers)

# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = urllib2.urlopen(req)

# 4. 打印响应内容
print response.read()
```

- ![图片](../image/02.png)
  
- 但是这样做太过复杂，我们先需要在浏览器登录账户，并且设置保存密码，并且通过抓包才能获取这个Cookie，那有么有更简单方便的方法呢？

## cookielib库 和 HTTPCookieProcessor处理器

- 在Python处理Cookie，一般是通过cookielib模块和 urllib2模块的HTTPCookieProcessor处理器类一起使用。
  - cookielib模块：主要作用是提供用于存储cookie的对象
  - HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。

## cookielib 库

- python2 中为 cookielib, python3 为 http.cookiejar
- 该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
  - CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
  
  - FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。

  - MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

  - LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。

- **其实大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()**

- 我们来做几个案例：

### 1. 获取Cookie，并保存到CookieJar()对象中

```python
from urllib import request
from http import cookiejar

# 构建一个CookieJar对象实例来保存cookie
cookiejar = cookiejar.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = request.build_opener(handler)

# 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
opener.open("http://www.baidu.com")

## 可以按标准格式将保存的Cookie打印出来
cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

## 舍去最后一位的分号
print cookieStr[:-1]
```

- 我们使用以上方法将Cookie保存到cookiejar对象中，然后打印出了cookie中的值，也就是访问百度首页的Cookie值。
- 运行结果如下：
    BAIDUID=4327A58E63A92B73FF7A297FB3B2B4D0:FG=1;BIDUPSID=4327A58E63A92B73FF7A297FB3B2B4D0;H_PS_PSSID=1429_21115_17001_21454_21409_21554_21398;PSTM=1480815736;BDSVRTM=0;BD_HOME=0

### 2. 访问网站获得cookie，并把获得的cookie保存在cookie文件中

```python

from urllib import request
from http import cookiejar

# 保存cookie的本地磁盘文件名
filename = 'cookie.txt'

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = cookiejar.MozillaCookieJar(filename)

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = request.build_opener(handler)

# 创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")

# 保存cookie到本地文件
cookiejar.save()
```

### 3. 从文件中获取cookies，做为请求的一部分去访问

```python
from urllib import request
from http import cookiejar

# 创建MozillaCookieJar(有load实现)实例对象
cookiejar = cookiejar.MozillaCookieJar()

# 从文件中读取cookie内容到变量
cookie.load('cookie.txt')

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)

# 通过 build_opener() 来构建opener
opener = request.build_opener(handler)

response = opener.open("http://www.baidu.com")
```

### 利用cookielib和post登录人人网

```python
from urllib import request, parse
from http import cookiejar

# 1. 构建一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()

# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = request.HTTPCookieProcessor(cookie)

# 3. 通过 build_opener() 来构建opener
opener = request.build_opener(cookie_handler)

# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# 5. 需要登录的账户和密码
data = {"email":"mr_mao_hacker@163.com", "password":"alaxxxxxime"}  

# 6. 通过urlencode()转码
postdata = parse.urlencode(data).encode()

# 7. 构建Request请求对象，包含需要发送的用户名和密码
request = urllib2.Request("http://www.renren.com/PLogin.do", data = postdata, method="POST")

# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
opener.open(request)

# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")  

# 10. 打印响应内容
print response.read()
```

## 模拟登录要注意几点

1. 登录一般都会先有一个HTTP GET，用于拉取一些信息及获得Cookie，然后再HTTP POST登录。
2. HTTP POST登录的链接有可能是动态的，从GET返回的信息中获取。
3. password 有些是明文发送，有些是加密后发送。有些网站甚至采用动态加密的，同时包括了很多其他数据的加密    信息，只能通过查看JS源码获得加密算法，再去破解加密，非常困难。
4. 大多数网站的登录整体流程是类似的，可能有些细节不一样，所以不能保证其他网站登录成功。

- 这个测试案例中，为了想让大家快速理解知识点，我们使用的人人网登录接口是人人网改版前的隐藏接口(嘘....)   ，登录比较方便。
- 当然，我们也可以直接发送账号密码到登录界面模拟登录，但是当网页采用JavaScript动态技术以后，想封锁基于   HttpClient 的模拟登录就太容易了，甚至可以根据你的鼠标活动的特征准确地判断出是不是真人在操作。
- 所以，想做通用的模拟登录还得选别的技术，比如用内置浏览器引擎的爬虫(关键词：Selenium ，PhantomJS)，这个我们将在以后会学习到。

## 案例

- test04_人人网状态保持.py
- 07_人人网获取cookie.py