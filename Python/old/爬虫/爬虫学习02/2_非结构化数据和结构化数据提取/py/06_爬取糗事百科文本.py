from urllib import request
import json
from lxml import etree


class QiuShiSpider:
    """
    糗事百科文本爬虫
    """
    def __init__(self, index):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.index = index
        self.url = "https://www.qiushibaike.com/text/page/" + str(index) + "/"


    def download_content(self):
        """
        抓取页面内容
        """
        req = request.Request(self.url, headers=self.headers)
        response = request.urlopen(req)
        html = response.read().decode()

        self.analysis_content(html)
    
    def analysis_content(self, html):
        """
        解析抓取到的页面内容
        """
        text = etree.HTML(html)

        # 使用xpath模糊查询查询到内容的大致范围，然后在这个范围内提取文本
        node_list = text.xpath('//div[contains(@id,"qiushi_tag_")]')

        for node in node_list:
            # xpath返回的查询结果是一个列表
            author = node.xpath('.//h2')[0].text
            content = node.xpath(".//div[@class='content']/span")[0].text
            vote = node.xpath('.//div[@class="stats"]/span[1]/i')[0].text
            comments = node.xpath('.//div[@class="stats"]/span[2]/a/i')[0].text

            qiushi = {
                "作者": author,
                "内容": content,
                "好笑": vote,
                "评论": comments,
            }

            self.write_content(qiushi)


    def write_content(self, qiushi_content):
        """
        将解析后的内容写入文件 
        """
        filename = "../text/糗事百科文本/第{}页.json".format(self.index)
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(json.dumps(qiushi_content, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    
    index = input("请输入想要爬取的页数：")

    qs = QiuShiSpider(index)
    qs.download_content()

