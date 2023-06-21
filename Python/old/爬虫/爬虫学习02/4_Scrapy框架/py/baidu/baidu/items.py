# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BaiduTiebaItem(scrapy.Item):
    """
    title: 每个贴的标题
    url: 每个贴的url
    image_list: 图片列表
    iaage_path: 图片路径
    name: 图片名
    """
    title = scrapy.Field()
    url = scrapy.Field()
    image_list = scrapy.Field()
    image_path = scrapy.Field()
    name = scrapy.Field()