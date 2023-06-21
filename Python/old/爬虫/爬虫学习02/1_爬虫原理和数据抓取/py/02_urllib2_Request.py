import urllib.request


url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
}
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

html = response.read()
html = html.decode("utf-8")

print(type(html))

with open("../html/baidu2.html", 'w', encoding="utf-8") as f:
    f.write(html)
    print("success")