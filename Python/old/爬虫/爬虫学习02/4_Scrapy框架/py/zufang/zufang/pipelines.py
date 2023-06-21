# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ZufangPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        self.filename = open("./json/zufang.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        item = json.dumps(dict(item), ensure_ascii=False)
        self.filename.write(item + "\n")
        return item

    def close_spider(self, spider):
        self.filename.close()