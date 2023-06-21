from urllib import request, parse


url = "https://www.baidu.com/s?"

word = input("请输入关键词：")

keyword = {"wd": word}

# 转换成url编码格式
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


