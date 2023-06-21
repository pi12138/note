# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubanmovieItem


class Movietop2502Spider(CrawlSpider):
    name = 'movietop250_2'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
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



