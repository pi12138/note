# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class ReadSpider(scrapy.Spider):
    name = 'read'
    allowed_domains = ['douban.com']
    start_urls = ['https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban']

    def parse(self, response):
        a_list = response.xpath('//ul[@class="list kinds-list tab-panel"]/li/a')

        for a in a_list:
            item = {}

            item['first_title'] = a.xpath('./text()').extract_first()
            item['first_url'] = a.xpath('./@href').extract_first()
            # item['first_url']需要进行一些处理
            item['first_url'] = self.handle_first_url(item['first_url'])

            yield scrapy.Request(
                url=item['first_url'],
                callback=self.parse_second,
                meta={'item': deepcopy(item)}
            )

    def parse_second(self, response):
        item = response.meta['item']

        a_list = response.xpath('//ul[@class="works-list"]/li//h4[@class="title"]/a')

        for a in a_list:
            item['book_title'] = a.xpath('./@title').extract_first()
            item['book_url'] = a.xpath('./@href').extract_first()

            yield scrapy.Request(
                url="https://read.douban.com"+item['book_url'],
                callback=self.parse_third,
                meta={'item': deepcopy(item)}
            )

    def parse_third(self, response):
        item = response.meta['item']

        infos = response.xpath('//div[@class="article-profile-bd"]')

        item['author'] = infos.xpath('.//p[@class="author"]/span[2]/a/text()').extract_first()
        item['score'] = infos.xpath('.//div[@class="rating rating-light"]//span[@class="score"]/text()').extract_first()
        item['price'] = response.xpath('//span[@class="current-price-count"]/text()').extract_first()
        item['info'] = response.xpath('//div[@class="info"]/p/text()').extract()

        print(item)

    def handle_first_url(self, url):
        """处理一级url，使其变成一个可以使用的url"""
        url = url[1:]
        url = "https://read.douban.com/category/?" + url.replace('/', '=')

        return url
