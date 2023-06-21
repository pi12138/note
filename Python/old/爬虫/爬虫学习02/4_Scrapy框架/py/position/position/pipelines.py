# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class PositionPipeline(object):
#     # def process_item(self, item, spider):
#     #     return item
#
#     def __init__(self):
#         self.file = open('tencent_position.json', 'w', encoding="utf-8")
#
#     def process_item(self, item, spider):
#         text = json.dumps(dict(item), ensure_ascii=False)
#         self.file.write(text + "\n")
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()


class Tencent3Pipeline(object):

    def process_item(self, item, spider):
        if spider.name == "tencent3":
            data = json.dumps(dict(item), ensure_ascii=False)

            with open('tencent3_position.json', 'a', encoding="utf-8") as f:
                f.write(data + "\n")

            return item

