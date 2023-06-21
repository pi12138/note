# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class JianguanSpider(CrawlSpider):
    name = 'jianguan'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab7324/']

    rules = (
        Rule(LinkExtractor(allow=r'/web/site0/tab7324/info.*?\.htm'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r"/web/site0/tab7324/module25157/page.*?\.htm"), follow=True),
    )

    def parse_item(self, response):
        item = {}

        item['title'] = re.findall(r"<!--TitleStart-->(.*?)<!--TitleEnd-->", response.body.decode())
        if item['title']:
            item['title'] = item['title'][0]

        contents = response.xpath('//table[@id="tab_content"]//tr[4]//span/p/text()').extract()
        item['content'] = ""

        for i in contents:
            item['content'] = item['content'] + i
        item['content'] = self.handle_content(item['content'])
        print(item)

    def handle_content(self, content):
        str_dict = {
            '\r\n': '',
            '\t': "",
            '\xa0': "",
            '\r': "",
            '\n': "",
        }

        contents = ''.join(content)
        for i in str_dict.keys():
            contents = contents.replace(i, str_dict[i])

        return contents
