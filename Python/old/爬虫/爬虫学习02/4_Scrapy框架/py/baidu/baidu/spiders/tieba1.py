# -*- coding: utf-8 -*-
import scrapy
from ..items import BaiduTiebaItem


class Tieba1Spider(scrapy.Spider):
    name = 'tieba1'
    allowed_domains = ['baidu.com']

    url = "https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn="
    offset = 0

    start_urls = [url+str(offset)]

    def parse(self, response):
        div_list = response.xpath('//ul[@id="thread_list"]//li[contains(@class, "j_thread_list")]/div')

        for div in div_list:
            item = BaiduTiebaItem()

            item['title'] = div.xpath('.//a[contains(@class, "j_th_tit")]/text()').extract_first()
            item['url'] = div.xpath('.//a[contains(@class, "j_th_tit")]/@href').extract_first()

            if item['url']:
                item['url'] = "https://tieba.baidu.com" + item['url']

            yield scrapy.Request(
                url=item['url'],
                callback=self.parse_page,
                meta={'item': item}
            )

        if self.offset < 250:
            self.offset += 50
            yield scrapy.Request(
                url=self.url+str(self.offset),
                callback=self.parse,
            )

    def parse_page(self, response):
        item = response.meta['item']

        item['image_list'] = []

        image_urls = response.xpath('//img[@size]')
        for img in image_urls:
            img_url = img.xpath('./@src').extract_first()
            if img_url:
                item['image_list'].append(img_url)

        yield item





