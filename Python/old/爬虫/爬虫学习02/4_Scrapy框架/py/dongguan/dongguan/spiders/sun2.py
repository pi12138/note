# -*- coding: utf-8 -*-
import scrapy
from ..items import DongguanItem


class Sun2Spider(scrapy.Spider):
    name = 'sun2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    def parse(self, response):
        tr_list = response.xpath('//div[@class="greyframe"]//tr//tr')

        for tr in tr_list:
            item = DongguanItem()

            item['number'] = tr.xpath('./td[1]/text()').extract_first()
            item['title'] = tr.xpath('./td[2]/a[2]/text()').extract_first()
            item['status'] = tr.xpath('./td[3]/span/text()').extract_first()
            item['name'] = tr.xpath('./td[4]/text()').extract_first()
            item['url'] = tr.xpath('./td[2]/a[2]/@href').extract_first()
            item['date'] = tr.xpath('./td[5]/text()').extract_first()

            yield scrapy.Request(url=item['url'], callback=self.parse_page, meta={'item': item})

        next_btn = response.xpath('//div[@class="pagination"]/a[text()=">"]/@href').extract_first()
        if next_btn is not None:
            yield scrapy.Request(url=next_btn, callback=self.parse)

    def parse_page(self, response):
        """处理每个页面详细页内容"""
        item = response.meta['item']

        img = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/div[1]/img/@src').extract()

        # 如果img是一个空列表，则代表该页面无图片
        if img:
            item['content'] = response.xpath(
                '//div[@class="wzy1"]/table[2]//tr[1]/td/div[@class="contentext"]/text()').extract()
            item['content_img'] = ['http://wz.sun0769.com'+i for i in img]
        else:
            item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()
            item['content_img'] = None

        yield item
