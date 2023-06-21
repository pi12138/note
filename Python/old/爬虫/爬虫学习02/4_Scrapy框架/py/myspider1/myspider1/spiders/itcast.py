# -*- coding: utf-8 -*-
import scrapy
from myspider1.items import Myspider1Item


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        # with open("itcast.html", 'w', encoding="utf-8") as f:
        #     f.write(response.body.decode())
        #
        node_list = response.xpath('//div[@class="li_txt"]')

        # items = []
        for node in node_list:
            item = Myspider1Item()

            # xpath 返回的数据是列表
            name = node.xpath('./h3/text()').extract()
            level = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()

            item["name"] = name[0]
            item["level"] = level[0]
            item["info"] = info[0]

            yield item

            # items.append(item)

        # return items

    """
    两种返回数据的方式
        1. 将 模型实例化对象 添加到一个 列表中最后使用return一次性返回
        2. 将 模型实例化对象 使用 yield 一个一个返回(一个一个交给pipelines管道文件，需要编写piplines.py 文件)
    """