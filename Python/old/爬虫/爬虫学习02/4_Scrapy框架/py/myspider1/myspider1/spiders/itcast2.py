# -*- coding: utf-8 -*-
import scrapy
from ..items import Myspider1Item


class Itcast2Spider(scrapy.Spider):
    name = 'itcast2'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        li_list = response.xpath('//div[@class="tea_con"]//li')

        for li in li_list:
            item = Myspider1Item()

            item['name'] = li.xpath('.//h3/text()').extract_first()
            item['level'] = li.xpath('.//h4/text()').extract_first()
            item['info'] = li.xpath('.//p/text()').extract_first()

            yield item
