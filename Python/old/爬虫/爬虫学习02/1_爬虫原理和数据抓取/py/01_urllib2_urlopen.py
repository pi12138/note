import urllib.request

url = "http://www.baidu.com/"

# 向指定url 发送请求，并返回服务器响应的 类文件对象
response = urllib.request.urlopen(url)


# 类文件对象 支持 文件对象的操作方法。如 read（）方法读取文件的全部内容，返回字符串
html = response.read()

html = html.decode("utf-8")
# print(html)
print(type(html))


with open("../html/baidu.html", "w", encoding="utf-8") as f:
    f.write(html)
    print("success")
