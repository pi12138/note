# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    first_title = scrapy.Field()
    first_url = scrapy.Field()

    second_title = scrapy.Field()
    second_url = scrapy.Field()

    third_title = scrapy.Field()
    third_url = scrapy.Field()
    third_content = scrapy.Field()

    file_path = scrapy.Field()
