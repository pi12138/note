# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaItem
import os
from copy import deepcopy


class MySpider(scrapy.Spider):
    name = "sina_news"
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://news.sina.com.cn/guide/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="tab01"]/div')

        for div in div_list[0:-1]:
            item = SinaItem()

            item['first_title'] = div.xpath('./h3/a/text()').extract_first()
            item['first_url'] = div.xpath('./h3/a/@href').extract_first()

            file_path1 = './data/{}/'.format(item['first_title'])
            if os.path.exists(file_path1):
                pass
            else:
                os.mkdir(file_path1)

            li_list = div.xpath('./ul/li')

            for li in li_list:
                item['second_title'] = li.xpath('./a/text()').extract_first()
                item['second_url'] = li.xpath('./a/@href').extract_first()

                file_path2 = file_path1 + "{}/".format(item['second_title'])
                if os.path.exists(file_path2):
                    pass
                else:
                    os.mkdir(file_path2)

                yield scrapy.Request(
                    url=item['second_url'],
                    callback=self.parse_second,
                    meta={'item': deepcopy(item)})

    def parse_second(self, response):
        item = response.meta['item']

        a_list = response.xpath('//a[contains(@href, "2019-04-16")]')

        for a in a_list:
            item['third_url'] = a.xpath('./@href').extract_first()

            yield scrapy.Request(url=item['third_url'],
                                 callback=self.parse_third,
                                 meta={'item': deepcopy(item)})

    def parse_third(self, response):
        item = response.meta['item']

        item['third_title'] = response.xpath('//h1[@class="main-title"]/text()').extract_first()
        item['third_content'] = response.xpath('//div[@id="article"]//p/text()').extract()
        # item['content_img'] = response.xpath('//div[@id="article"]/div[@class="img_wrapper"]/img').etxract()

        yield item

