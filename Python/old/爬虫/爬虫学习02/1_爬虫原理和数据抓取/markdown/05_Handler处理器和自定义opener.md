# Handler处理器 和 自定义Opener

- opener是 urllib.request.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

- 但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
    1. 使用相关的 Handler处理器 来创建特定功能的处理器对象;
    2. 然后通过 urllib.request.build_opener()方法使用这些处理器对象，创建自定义opener对象；
    3. 使用自定义的opener对象，调用open()方法发送请求。

- 如果程序里所有的请求都使用自定义的opener，可以使用urllib.request.install_opener() 将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

## 简单的自定义opener()

```python
import urllib

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib.request.HTTPHandler()

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = urllib.request.HTTPSHandler()

# 调用urllib.request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler)

# 构建 Request请求
request = urllib.request.Request("http://www.baidu.com/")

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

# 获取服务器响应内容
print(response.read())
```

- 这种方式发送请求得到的结果，和使用urllib.request.urlopen()发送HTTP/HTTPS请求得到的结果是一样的。

- 如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作。

```python
# 仅需要修改的代码部分：

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
http_handler = urllib.request.HTTPHandler(debuglevel=1)

# 构建一个HTTPHSandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
https_handler = urllib.request.HTTPSHandler(debuglevel=1)
```

## 案例

- 04_自定义一个简单的opener().py