# urllib默认只支持HTTP/HTTPS的GET和POST方

- 一般HTTP请求提交数据，需要编码成 URL编码格式，然后做为url的一部分，或者作为参数传到Request对象中。
- 在Python2.X中，分urllib和urllib2，但在Python3.X中，都统一合并到urllib中。
- [Python2.x和Python3.x urllib的区别](https://blog.csdn.net/fly910905/article/details/83418623)
- 在Python3中 编码 使用 urllib.parse.urlencode() 函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，
- 解码 工作可以使用urllib.parse.unquote()函数

- **注：urlencode()的参数为一个字典**

## GET

- GET请求一般用于我们向服务器获取数据，比如说，我们用百度搜索传智播客：`https://www.baidu.com/s?wd=传智播客`
- 浏览器的url会跳转 `https://www.baidu.com/s?wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2`
- 在其中我们可以看到在请求部分里，`http://www.baidu.com/s?` 之后出现一个长长的字符串，其中就包含我们要查询的关键词传智播客，于是我们可以尝试用默认的Get方式来发送请求。

```python
from urllib import request, parse


url = "https://www.baidu.com/s?"

word = input("请输入关键词：")

keyword = {"wd": word}

# 转换成url编码格式,注意 urlencode() 方法的参数
keyword = parse.urlencode(keyword)

fullurl = url + keyword

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

req = request.Request(fullurl, headers=headers)

response = request.urlopen(req)

html = response.read().decode()

with open("../html/baidu3.html", 'w', encoding="utf-8") as f:
    f.write(html)
    print("success")
```

## get请求和Post请求的区别

- get:   请求的 url 会附带查询参数，查询参数在 QueryString 里保存
- post:  请求的 url 不会附带参数, 查询参数在 Form 表单里保存

## POST方式：

- 上面我们说了Request请求对象的里有data参数，它就是用在POST里的，我们要传送的数据就是这个参数data，data是一个字典，里面要匹配键值对。
- urllib.request.Request() 想要发送 POST 请求, 需要注意的几点
  - data 参数需要先转码，然后在进行编码, urllib.parse.urlencode(data).encode()
  - method 参数的值为 "POST", method = "POST"
  - Request(url, data=data, headers=headers, method="POST")
  
- 发送POST请求时，需要特别注意headers的一些属性：
  - Content-Length: 144： 是指发送的表单数据长度为144，也就是字符个数是144个。
  - X-Requested-With: XMLHttpRequest ：表示Ajax异步请求。
  - Content-Type: application/x-www-form-urlencoded ： 表示浏览器提交 Web 表单时使用，表单数据会按照 name1=value1&name2=value2 键值对形式进行编码。

```python3
from urllib import parse, request

url = "xxxxxxxxx"

data = {"key1": "value1"}

headers = {"User-Agent":"xxxx"}

data = parse.urlencode(data).encode("utf-8")

req = request.Request(url, data=data, headers=headers, method="POST")

response = request.urlopen(req)

html = response.read().decode()

print(html)

```

## 案例

- 03_urllib_发送get请求方式.py
- test01_爬取贴吧页面数据.py                (发送get请求练习)
- test02_通过有道词典制作英文转中文翻译器.py   (发送post请求练习)