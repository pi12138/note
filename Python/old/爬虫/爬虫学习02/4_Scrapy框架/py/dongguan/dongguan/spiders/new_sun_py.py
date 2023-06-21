# -*- coding: utf-8 -*-
"""
sun.py 完善版本
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DongguanItem


class NewSunPySpider(CrawlSpider):
    name = 'new_sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    links1 = LinkExtractor(allow=r"type=4")
    links2 = LinkExtractor(allow=r"/question/201904/\d+.shtml")

    rules = (
        # 调用 handle_urls 处理每个页面里的链接
        Rule(links1, process_links="handle_urls", follow=True),
        Rule(links2, callback='parse_item', follow=False)
    )

    # 当访问量过大时，服务器会返回不合格的url
    # 处理不合格的url，将其处理为合格的url
    def handle_urls(self, links):
        for link in links:
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
        return links

    def parse_item(self, response):
        item = DongguanItem()

        item['title'] = self.get_title(response)
        item['number'] = self.get_number(response)
        item['content'] = self.get_content(response)
        # item['process_status'] = self.get_process_status(response)
        item['url'] = response.url

        yield item

    def get_title(self, response):
        """获取标题"""
        title = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"]').extract()[0]
        return title.split("：")[-1]

    def get_number(self, response):
        """获取编号"""
        number = response.xpath('//div[@class="wzy1"]//td[@valign="middle"]/span[2]/text()').extract()[0]
        return number.split(":")[-1]

    def get_content(self, response):
        """获取内容"""
        contents = response.xpath('//div[@class="wzy1"]//div[@class="contentext"]/text()').extract()

        # 对获取到的内容进行处理
        # xpath返回的是一个列表，对列表内容拼接成字符串
        if len(contents) == 0:
            contents = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"]/text()').extract()

        content = self.handle_str("".join(contents))

        return content

    def handle_str(self, text):
        """处理字符串"""
        replace_rule = ["\r\n", "\t", "\xa0"]

        for key in replace_rule:
            text = text.replace(key, "")

        return text

