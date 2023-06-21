# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanmovieItem


class Movietop2501Spider(scrapy.Spider):
    name = 'movietop250_1'
    allowed_domains = ['movie.douban.com']

    offset = 0
    url = 'https://movie.douban.com/top250?start={}&filter='

    start_urls = [url.format(offset), ]

    def parse(self, response):
        # pass
        nodes = response.xpath('//ol[@class="grid_view"]/li')

        for node in nodes:
            item = DoubanmovieItem()

            ranking = node.xpath('.//em/text()').extract()[0]
            title = node.xpath('.//span[@class="title"][1]/text()').extract()[0]
            rating_num = node.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            # inq = node.xpath('.//span[@class="inq"]/text()').extract()
            inq = self.handle_inq(node)

            item['title'] = title
            item['ranking'] = ranking
            item['rating_num'] = rating_num
            item['inq'] = inq

            yield item

        if self.offset < 225:
            self.offset += 25

            yield scrapy.Request(self.url.format(self.offset), callback=self.parse)

    def handle_inq(self, node):
        """
        处理简介信息，某些简介信息为空
        """
        inq = node.xpath('.//span[@class="inq"]/text()').extract()

        # 如果 inq 不是一个空列表，则相当于True
        # 如果 inq 为一个空列表，则相当于False
        if inq:
            return inq[0]
        else:
            return inq
