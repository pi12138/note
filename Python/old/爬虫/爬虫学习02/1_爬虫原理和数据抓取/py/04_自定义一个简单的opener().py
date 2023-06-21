from urllib import request, parse

# 1. 创建一个http处理器对象
# http_handler = request.HTTPHandler()

# 在HTTPHandler() 中增加参数 debuglevel=1 将会自动打开 Debug log 模式
# 程序在执行时会自动打印收发包信息，可以用来调试
http_handler = request.HTTPHandler(debuglevel=1)

# 2. 创建自定义opener对象
opener = request.build_opener(http_handler)

# 3. 调用opener对象的open()方法
response = opener.open("http://www.baidu.com")

# print(response.read().decode())

# response2 = opener.open("https://www.baidu.com")

# print(response2.read().decode())
