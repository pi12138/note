# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.conf import settings


# 存文件
class DoubanmoviePipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        self.file = open('./downloadfile/top250_2.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False)

        self.file.write(text + '\n')

        return item

    def close_spider(self, spider):
        self.file.close()


# 存mysql
# class DoubanmoviePipeline(object):
#     def __init__(self):
#         host = settings['HOST']
#         port = settings['PORT']
#         user = settings['USER']
#         pwd = settings['PASSWORD']
#         db_name = settings['DB_NAME']
#
#         self.connect = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db_name)
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         table_name = settings['TABLE_NAME']
#         sql = 'INSERT INTO {0}(ranking, title, rating_num, inq) VALUES({1}, "{2}", "{3}", "{4}");'.format(table_name, int(item['ranking']), item['title'], item['rating_num'], item['inq'])
#
#         self.cursor.execute(sql)
#         self.connect.commit()
#
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.connect.close()