# -*- coding: utf-8 -*-
"""
存在问题，该网站有一定的反爬虫机制
会提供错误的url，导致爬虫无法继续拿到数据
详情修改见：new_sun.py
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    linkextractor1 = LinkExtractor(allow=r"type=4&page=\d+")
    linkextractor2 = LinkExtractor(allow=r"/question/201904/\d+.shtml")

    rules = (
        Rule(linkextractor1, follow=True),
        Rule(linkextractor2, callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        item = DongguanItem()

        item['title'] = self.get_title(response)
        item['number'] = self.get_number(response)
        item['content'] = self.get_content(response)
        # item['process_status'] = self.get_process_status(response)
        item['url'] = response.url

        return item

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
        content = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"]/text()').extract()[0]
        return content

    # def get_process_status(self, response):
    #     """获取受理状态"""
    #     process_status = response.xpath('//div[@class="wzy1"]//span[@class="qgrn"]/text()').extract()[0]
    #     return process_status


