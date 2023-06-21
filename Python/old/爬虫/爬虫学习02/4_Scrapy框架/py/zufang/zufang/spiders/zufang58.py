# -*- coding: utf-8 -*-
# 58同城租房，杭州板块第一页
import scrapy
from zufang.items import ZufangItem


class Zufang58Spider(scrapy.Spider):
    name = 'zufang58'
    allowed_domains = ['hz.58.com']
    start_urls = ['https://hz.58.com/chuzu/']

    def parse(self, response):
        # pass

        node_list1 = response.xpath('//ul[@class="listUl"]/li[@logr]')
        # 下面匹配不到内容
        # node_list2 = response.xpath('//ul[@class="listUl"]/li[@class="apartments"]')

        for node in node_list1:
            item1 = ZufangItem()

            title = node.xpath('.//h2/a/text()').extract()
            info = node.xpath('.//p[contains(@class, "room")]/text()').extract()
            address = node.xpath('.//p[contains(@class, "add")]/text()').extract()
            from_ = node.xpath('.//div[@class="jjr"]/text()|.//p[@class="geren"]/text()').extract()
            price = node.xpath('.//div[@class="money"]/b/text()').extract()

            item1['title'] = title[0]
            item1['info'] = info[0]
            item1['address'] = address[0]
            item1['from_'] = from_[0]
            item1['price'] = price[0]

            yield item1

        # 上面的xpath 未匹配到内容
        # for node in node_list2:
        #
        #     item2 = ZufangItem()
        #
        #     title = node.xpath('.//h2/a/text()').extract()
        #     info = node.xpath('.//p[contains(@class, "room")]/text()').extract()
        #     address = node.xpath('.//p[contains(@class, "add")]/text()').extract()
        #     from_ = node.xpath('.//p[@class="gongyu"]/text()').extract()
        #     price = node.xpath('.//div[@class="money"]/b/text()').extract()
        #
        #     item2['title'] = title[0]
        #     item2['info'] = info[0]
        #     item2['address'] = address[0]
        #     item2['from_'] = from_[0]
        #     item2['price'] = price[0]
        #
        #     yield item2

        # print("结尾")
