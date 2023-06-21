# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuappItem


class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0']

    def parse(self, response):
        # pass
        data = json.loads(response.body)['data']

        for info in data:
            item = DouyuappItem()

            item['name'] = info['nickname']
            item['image_url'] = info['room_src']

            yield item