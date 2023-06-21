# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QiushibaikePipeline(object):
    # def process_item(self, item, spider):
        # return item

    def __init__(self):
        self.file = open("qiushibaike.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(text + "\n")

        return item

    def close_spider(self, spider):
        self.file.close()

