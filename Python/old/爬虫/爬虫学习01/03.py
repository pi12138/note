# 查看urlopen返回对象
from urllib import request
import chardet

url = "http://www.baidu.com/"


response = request.urlopen(url)
print("response_type:", type(response))
print("response:", response)

print("response.geturl:", response.geturl())
print("response.info:", response.info())
print("response.getcode:", response.getcode())