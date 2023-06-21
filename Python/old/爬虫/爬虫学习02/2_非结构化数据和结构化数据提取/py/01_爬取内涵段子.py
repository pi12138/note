from urllib import request
import re


class DuanZhiSpider:
    """
    内涵段子类
    """
    def __init__(self, page):    
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.page = page
        self.switch = True
        self.fullurl = ""

    def load_page(self):
        """
        加载页面
        """
        url = "https://www.neihanba.com/dz/"

        if self.page == 1:
            self.fullurl = url + "index.html"
        else:
            self.fullurl = url + "list_" + str(self.page) + ".html"

        req = request.Request(self.fullurl, headers=self.headers)
        response = request.urlopen(req)
        html = response.read().decode("gbk")
        
        return html


    def write_page(self, html):
        """
        保存页面
        """
        with open(r"../text/第{}页.txt".format(self.page), 'w', encoding="utf-8") as f:
            for i in html:
                f.write(i+"\n")

        return "success"


    def handle_page(self, html):
        """
        处理页面内容
        """
        pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        content_list = pattern.findall(html)

        return content_list


    def strat_work(self):
        """
        控制爬虫
        """
        html = self.load_page()
        content_list = self.handle_page(html)
        self.write_page(content_list)

        while self.switch:
            command = input("按回车爬取下一页，输入quit退出：")
            
            if command == "quit":
                self.switch = False
            else:
                self.page += 1
                html = self.load_page()
                content_list = self.handle_page(html)
                self.write_page(content_list)



if __name__ == "__main__":

    index = input("请输入你想观看的页数：")

    dz = DuanZhiSpider(int(index))
    dz.strat_work()