# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Myspider1Pipeline(object):
    """管道类"""
    # def process_item(self, item, spider):
    #     # 该方法必须要有，
    #     # 作用是用来处理item数据
    #     with open("teachers2.json", 'a', encoding="utf-8") as f:
    #         f.write(json.dumps(dict(item), ensure_ascii=False))
    #
    #     return item

    def __init__(self):
        # __init__()方法可选，作为类的初始化方法
        self.filename = open("teachers2.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        # 必须
        self.filename.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        return item

    def close_spider(self, spider):
        # 可选，在结束时调用该方法
        self.filename.close()


class Itcast2Pipeline(object):
    """只处理 itcast2 爬虫数据"""

    def process_item(self, item, spider):
        if spider.name == "itcast2":
            data = json.dumps(dict(item), ensure_ascii=False)

            with open('itcast2.json', 'a', encoding='utf-8') as f:
                f.write(data + '\n')

            return item


