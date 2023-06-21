# -*- coding: utf-8 -*-
import scrapy
from ..items import PositionItem


class Tencent3Spider(scrapy.Spider):
    name = 'tencent3'
    allowed_domains = ['tencent.com']

    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]//tr[@class="even" or @class="odd"]')

        for tr in tr_list:
            item = PositionItem()

            item['position_name'] = tr.xpath('.//td[1]/a/text()').extract_first()
            item['position_url'] = tr.xpath('.//td[1]/a/@href').extract_first()
            item['position_type'] = tr.xpath('.//td[2]/text()').extract_first()
            item['position_num'] = tr.xpath('.//td[3]/text()').extract_first()
            item['position_place'] = tr.xpath('.//td[4]/text()').extract_first()
            item['position_date'] = tr.xpath('.//td[5]/text()').extract_first()

            yield item

        if self.offset < 3180:
            self.offset += 30

            yield scrapy.Request(url=self.url+str(self.offset), callback=self.parse)
