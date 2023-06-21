# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com', "p.3.cn"]
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//div[@class="mc"]/dl/dt')
        dd_list = response.xpath('//div[@class="mc"]/dl/dd')

        for i in range(0, len(dt_list)):
            item = {}

            item['first_title'] = dt_list[i].xpath('./a/text()').extract_first()
            em_list = dd_list[i].xpath('./em')

            for em in em_list:
                item['second_title'] = em.xpath('./a/text()').extract_first()
                item['second_url'] = em.xpath('./a/@href').extract_first()
                item['second_url'] = self.handle_second_url(item['second_url'])

                if item['second_url']:
                    yield scrapy.Request(
                        url=item['second_url'],
                        callback=self.parse_second,
                        meta={"item": deepcopy(item)}
                    )

    def parse_second(self, response):
        item = response.meta['item']

        div_list = response.xpath('//ul[contains(@class, "gl-warp")]/li/div')

        for div in div_list:
            item['book_name'] = div.xpath('./div[@class="p-name"]/a/em/text()').extract_first()
            item['book_price'] = div.xpath('./div[@class="p-price"]/strong[1]//i/text()').extract_first()
            item['book_words'] = div.xpath('./div[@class="p-name"]/a/@title').extract_first()
            item['book_url'] = div.xpath('./div[@class="p-name"]/a/@href').extract_first()

            item['book_name'] = self.handle_book_name(item['book_name'])
            item['book_url'] = self.handle_book_url(item['book_url'])

            sku = div.xpath('./@data-sku').extract_first()
            price_url = "https://p.3.cn/prices/mgets?skuIds=J_{}".format(sku)

            yield scrapy.Request(
                url=price_url,
                callback=self.parse_price,
                meta={'item': deepcopy(item)}
            )

        # 翻页
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_url:
            next_url = "https://list.jd.com" + next_url
            yield scrapy.Request(
                url=next_url,
                callback=self.parse_second,
                meta={'item': item}
            )

    def parse_price(self, response):
        """
        获取图书价格
        :param response: 价格页面的响应，主要内容为json格式
        :return:
        """
        item = response.meta['item']

        data = json.loads(response.body.decode())
        item['book_price'] = data[0]['op']

        print(item)

    def handle_second_url(self, url):
        """
        获取的url需要处理，处理url
        :param url: 需要处理的url
        :return: 处理后的url
        """
        if url:
            url = url.split('/')[-1]
            url = url[:-5]
            url_list = url.split('-')

            start_url = "https://list.jd.com/list.html?"
            end_url = "cat={0},{1},{2}&tid={3}".format(url_list[0], url_list[1], url_list[2], url_list[2])
            url = start_url+end_url

        return url

    def handle_book_name(self, book_name):
        """
        处理图书名中的换行符和空格
        :param book_name: 图书名
        :return: 处理后的图书名
        """
        if book_name:
            str_dict = {
                '\n': '',
                " ": "",
            }

            for i in str_dict.keys():
                book_name = book_name.replace(i, str_dict[i])

        return book_name

    def handle_book_url(self, book_url):
        """
        图书地址的url不完整，处理完整
        :param book_url: 图书的url
        :return: 处理后的url
        """
        if book_url:
            book_url = "https:" + book_url
        return book_url
