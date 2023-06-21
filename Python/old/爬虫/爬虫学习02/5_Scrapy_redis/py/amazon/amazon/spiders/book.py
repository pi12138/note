# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy


class BookSpider(RedisSpider):
    name = 'book'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.cn/']
    redis_key = "amazon_book"

    def parse(self, response):
        div_list = response.xpath('//div[@id="content"]/div[@class="a-row a-size-base"]')

        for div in div_list:
            item = {}

            item['first_title'] = div.xpath('./div[1]/h5/a/@title').extract_first()
            td_list = div.xpath('./div[2]//td')

            for td in td_list:
                item['second_title'] = td.xpath('./a/@title').extract_first()
                item['second_url'] = td.xpath('./a/@href').extract_first()

                if item['second_url']:
                    if "http://www.amazon.cn/" in item['second_url']:
                        yield scrapy.Request(
                            url=item['second_url'],
                            callback=self.parse_book_list,
                            meta={'item': deepcopy(item)}
                        )

    def parse_book_list(self, response):
        item = response.meta['item']

        li_list = response.xpath('//div[@id="mainResults"]/ul/li')

        for li in li_list:
            item['book_name'] = li.xpath('.//div[@class="a-row a-spacing-small"]/div[1]/a/@title').extract_first()
            item['book_author'] = li.xpath('.//div[@class="a-row a-spacing-small"]/div[2]/span/text()').extract()
            item['book_type'] = li.xpath('.//div[@class="a-column a-span7"]/div[@class="a-row a-spacing-none"][1]//text()').extract_first()
            item['book_price'] = li.xpath('.//div[@class="a-column a-span7"]/div[@class="a-row a-spacing-none"][2]/a//text()').extract_first()

            print(item)

        # 翻页
        next_url = response.xpath('(//a[text()="下一页"]|//a[@title="下一页"])/@href').extract_first()
        if next_url:
            next_url = "https://www.amazon.cn" + next_url

            yield scrapy.Request(
                url=next_url,
                callback=self.parse_book_list,
                meta={'item': item}
            )

