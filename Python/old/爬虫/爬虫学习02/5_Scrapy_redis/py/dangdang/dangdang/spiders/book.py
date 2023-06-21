# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy


class BookSpider(RedisSpider):
    name = 'book'
    redis_key = "dangdangbook"
    allowed_domains = ['dangdang.com']

    def parse(self, response):
        div_list = response.xpath('//div[@class="con flq_body"]/div')

        for div in div_list:
            item = {}

            # 一级标题
            item['first_title'] = div.xpath('./dl/dt//text()').extract()
            item['first_title'] = self.handle_title(item['first_title'])
            dl_list = div.xpath('.//dl[@class="inner_dl"]')

            for dl in dl_list:
                # 二级标题
                item['second_title'] = dl.xpath('./dt//text()').extract()
                item['second_title'] = self.handle_title(item['second_title'])
                a_list = dl.xpath('./dd/a')

                for a in a_list:
                    # 三级标题
                    item['third_title'] = a.xpath('./@title').extract_first()
                    item['third_url'] = a.xpath('./@href').extract_first()

                    if item['third_url']:
                        yield scrapy.Request(
                            url=item['third_url'],
                            callback=self.parse_book_list,
                            meta={'item': deepcopy(item)}
                        )

    def parse_book_list(self, response):
        item = response.meta['item']

        li_list = response.xpath('//ul[@class="bigimg"]/li')

        for li in li_list:
            item['book_name'] = li.xpath('./p[@class="name"]/a/@title').extract_first()
            item['book_author'] = li.xpath('./p[@class="search_book_author"]/span[1]//text()').extract()
            item['published_date'] = li.xpath('./p[@class="search_book_author"]/span[2]/text()').extract_first()
            item['book_press'] = li.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            item['book_price'] = li.xpath('./p[@class="price"]/span[1]/text()').extract_first()
            item['book_detail'] = li.xpath('./p[@class="detail"]/text()').extract_first()

            print(item)

        # 翻页
        next_url = response.xpath('//a[@title="下一页"]/@href').extract_first()
        if next_url:
            next_url = "http://category.dangdang.com" + next_url

            yield scrapy.Request(
                url=next_url,
                callback=self.parse_book_list,
                meta={'item': item}
            )

    def handle_title(self, title):
        new_title = [t.strip() for t in title if len(t.strip()) > 0]

        return new_title
