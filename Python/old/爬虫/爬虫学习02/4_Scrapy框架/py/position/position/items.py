# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PositionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    """
    position_name: 职位名
    position_url: 职位链接
    position_type: 职位类型
    position_num: 职位数
    position_place: 职位地点
    position_date: 职位时间
    """

    position_name = scrapy.Field()
    position_url = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    position_place = scrapy.Field()
    position_date = scrapy.Field()
