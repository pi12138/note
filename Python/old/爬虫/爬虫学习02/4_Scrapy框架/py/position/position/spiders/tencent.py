# -*- coding: utf-8 -*-
import scrapy
from ..items import PositionItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # pass
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for node in node_list:
            item = PositionItem()

            position_name = node.xpath('./td[1]/a/text()').extract()[0]
            position_url = node.xpath('./td[1]/a/@href').extract()[0]
            position_type = node.xpath('./td[2]/text()').extract()[0]
            position_num = node.xpath('./td[3]/text()').extract()[0]
            position_place = node.xpath('./td[4]/text()').extract()[0]
            position_date = node.xpath('./td[5]/text()').extract()[0]

            item['position_name'] = position_name
            item['position_url'] = position_url
            item['position_type'] = position_type
            item['position_num'] = position_num
            item['position_place'] = position_place
            item['position_date'] = position_date

            yield item

        if self.offset < 300:
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
