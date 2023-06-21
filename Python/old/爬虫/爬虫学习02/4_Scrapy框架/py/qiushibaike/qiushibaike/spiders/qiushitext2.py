# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import QiushibaikeItem


class Qiushitext2Spider(CrawlSpider):
    name = 'qiushitext2'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    link_extractor = LinkExtractor(allow=r"/text/page/\d+/")

    rules = (
        Rule(link_extractor, callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        data_list = response.xpath("//div[contains(@id, 'qiushi_tag_')]")

        for data in data_list:
            item = QiushibaikeItem()

            name = data.xpath(".//h2/text()").extract()[0]
            content = data.xpath(".//div[@class='content']/span/text()").extract()[0]
            vote = data.xpath(".//span[@class='stats-vote']/i/text()").extract()[0]
            comment = data.xpath(".//span[@class='stats-comments']/a/i/text()").extract()[0]

            item['name'] = name
            item['content'] = content
            item['vote'] = vote
            item['comment'] = comment

            yield item
