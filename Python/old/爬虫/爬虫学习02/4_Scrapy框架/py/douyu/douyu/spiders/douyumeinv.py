# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem


class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['douyu.com']

    url = "https://www.douyu.com/gapi/rknc/directory/yzRec/1"

    start_urls = [url]

    def parse(self, response):
        # pass

        data = json.loads(response.text)["data"]
        data = data['rl']

        for info in data:
            item = DouyuItem()

            item['name'] = info['nn']
            item['image_url'] = info['rs16']

            yield item

