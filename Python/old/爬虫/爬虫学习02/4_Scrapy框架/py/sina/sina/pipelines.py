# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

# class SinaPipeline(object):
#     def process_item(self, item, spider):
#
#         file_path = item['file_path']
#         file_name = item['third_title']
#         content = item['third_content']
#
#         with open(file_path+file_name+".txt", 'w', encoding="utf-8") as f:
#             f.write(content)
#
#         return item


class SinaPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "sina_news":
            filepath = "./data/{0}/{1}/".format(item['first_title'], item['second_title'])

            if item['third_title'] is not None:
                filename = item['third_title'] + '.txt'
                content = ''.join(item['third_content'])

                with open(filepath+filename, 'w', encoding='utf-8') as f:
                    f.write(content)

        return item