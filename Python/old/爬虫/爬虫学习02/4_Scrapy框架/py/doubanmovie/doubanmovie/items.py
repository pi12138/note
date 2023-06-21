# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    """
    title: 标题
    ranking: 排行
    rating_num: 评分
    inq: 简介
    """
    title = scrapy.Field()
    ranking = scrapy.Field()
    rating_num = scrapy.Field()
    inq = scrapy.Field()