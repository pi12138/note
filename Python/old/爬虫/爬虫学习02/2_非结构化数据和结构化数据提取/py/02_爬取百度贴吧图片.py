from urllib import request, parse
from lxml import etree


class TieBaSpider:
    """
    爬取百度贴吧图片
    """

    def __init__(self, keyword, start, end):
        self.url = "http://tieba.baidu.com"
        self.keyword = keyword
        self.start = start
        self.end = end
        self.fullurl = ""
        self.headers = {
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
    

    def load_page(self):
        """
        加载贴吧页面
        """
        for i in range(self.start, self.end):
            self.keyword = parse.urlencode({"kw":self.keyword, "pn":i*50})
            self.fullurl = self.url + "/f?" + self.keyword
            # print(self.fullurl)

            # 不能传入headers ？？？？ 传入后 xpath提取不到内容
            # req = request.Request(self.fullurl, headers=self.headers)
            req = request.Request(self.fullurl)
            response = request.urlopen(req)

            html = response.read().decode()

            # with open("../html/baidu/第{}页.html".format(i+1), 'w', encoding="utf-8") as f:
            #     f.write(html)

            self.handle_page(html)


    def handle_page(self, html):
        """
        处理页面，提取每个楼主的url
        然后根据每个楼主页面的url提取其中图片的src
        html:贴吧页面
        """
        html = etree.HTML(html)
        landlord_urls = html.xpath('//a[@class="j_th_tit "]/@href')
        print(len(landlord_urls))

        for landlord in landlord_urls:
            landlord_url = self.url + landlord
            # print(landlord_url)

            req = request.Request(landlord_url)
            response = request.urlopen(req)
            html = response.read().decode()

            html = etree.HTML(html)
            image_urls = html.xpath('//img[@class="BDE_Image"]/@src')
            # print(len(image_urls))            
            length = len(image_urls)

            if  length == 0:
                pass
            else:
                for i in range(0, length):
                    self.download_page(image_urls[i])

            
    def download_page(self, url):
        """
        下载图片
        url:每个楼主页面的图片的src
        """
        req = request.Request(url)
        response = request.urlopen(req)
        html = response.read()

        filename = url[-10:]
        with open(r"../html/baidu/" + filename, 'wb') as f:
            f.write(html)
            print("{}下载完成！".format(f.name))


if __name__ == "__main__":
    keyword = input("请输入关键词：")
    start = input("请输入开始的页数：")
    end = input("请输入结束页数：")

    tb = TieBaSpider(keyword, int(start)-1, int(end))
    tb.load_page()