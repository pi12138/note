# -*- coding: utf-8 -*-
import scrapy
from ..items import DongguanItem


class SpiderSunSpider(scrapy.Spider):
    name = 'spider_sun'
    allowed_domains = ['wz.sun0769.com']

    offset = 90
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    start_urls = [url + str(offset)]
    # http://wz.sun0769.com/index.php/question/questionType?type=4&page=210

    def parse(self, response):
        """
        提取每个版面内的投诉信息的url
        """
        links = response.xpath('//div[@class="pagecenter"]//a[@class="news14"]/@href').extract()

        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        if self.offset < 210:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        """
        提取投诉信息内容
        """
        item = DongguanItem()

        item['title'] = self.get_title(response)
        item['number'] = self.get_number(response)
        item['content'] = self.get_content(response)
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
