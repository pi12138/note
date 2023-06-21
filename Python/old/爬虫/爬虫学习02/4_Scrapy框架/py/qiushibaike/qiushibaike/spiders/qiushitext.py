# -*- coding: utf-8 -*-
import scrapy
from ..items import QiushibaikeItem


class QiushitextSpider(scrapy.Spider):
    name = 'qiushitext'
    allowed_domains = ['qiushibaike.com']

    offset = 1
    url = 'https://www.qiushibaike.com/text/page/'

    start_urls = [url + str(offset) + "/"]

    def parse(self, response):
        # pass

        content_list = response.xpath("//div[contains(@id, 'qiushi_tag_')]")

        for data in content_list:
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

        if self.offset <= 13:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset) + "/", callback=self.parse)