"""
只爬取导航页【http://news.sina.com.cn/guide/】
新闻板块下的内容
"""

# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaItem
import os


class NewsNewsSpider(scrapy.Spider):
    name = 'news_news'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        # item = SinaItem()

        first_title = response.xpath('//div[@id="tab01"]/div[1]/h3/a/text()').extract()[0]
        first_url = response.xpath('//div[@id="tab01"]/div[1]/h3/a/@href').extract()[0]

        file_path1 = './data/{}/'.format(first_title)

        if os.path.exists(file_path1):
            pass
        else:
            os.mkdir(file_path1)

        title_list = response.xpath('//div[@id="tab01"]/div[1]/ul/li/a')

        for t in title_list:
            second_title = t.xpath('./text()').extract()[0]
            second_url = t.xpath('./@href').extract()[0]

            file_path2 = file_path1 + second_title + '/'

            if os.path.exists(file_path2):
                pass
            else:
                os.mkdir(file_path2)

            info = {
                'file_path': file_path2,
            }

            yield scrapy.Request(url=second_url, callback=self.parse_second_page, meta=info)

    def parse_second_page(self, response):
        a_list = response.xpath('//a[contains(@href, "https://news.sina.com.cn/c/")]/@href').extract()

        info = {
            "file_path": response.meta['file_path']
        }

        for a in a_list:
            yield scrapy.Request(url=a, callback=self.parse_third_page, meta=info)

    def parse_third_page(self, response):
        third_title = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
        content_list = response.xpath('//div[@id="article"]/p/text()').extract()

        third_content = ""
        for c in content_list:
            third_content += c

        item = SinaItem()

        item['third_title'] = third_title
        item['third_content'] = third_content
        item['file_path'] = response.meta['file_path']

        yield item



