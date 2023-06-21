"""不能爬取知乎"""
from urllib import request, parse
from bs4 import BeautifulSoup
from http import cookiejar

class ZhiHuSpider:
    """
    知乎爬虫
    """
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.url = "https://www.zhihu.com/signup?next=%2F"
        self.login_url = "https://www.zhihu.com/api/v3/oauth/sign_in"    
        self.data = {
            "username": "18790065681",
            "password": "zhou19981118",
        }

    def load_signup_page(self):
        """
        加载登录页面
        """
        # 设置cookie处理器，获取cookie值
        cookie = cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)

        req = request.Request(self.url, headers=self.headers)
        # response = request.urlopen(req)
        response = opener.open(req)
        # html = response.read().decode()

        # print(cookie)

        for c in cookie:
            # print(c)
            # print(c.name, c.value)
            self.data[c.name] = c.value

        # soup = BeautifulSoup(html, 'lxml')
        # soup.select("input[class")
        print(self.data)

        data = parse.urlencode(self.data).encode()

        req = request.Request(self.login_url, data=data, headers=self.headers, method="POST")
        response = opener.open(req)
        html = response.read().decode()

        with open("../html/zhihu.html", 'w', encoding="utf-8") as f:
            f.write(html)
            print("save success")
        
        

if __name__ == "__main__":
    zh = ZhiHuSpider()
    zh.load_signup_page()