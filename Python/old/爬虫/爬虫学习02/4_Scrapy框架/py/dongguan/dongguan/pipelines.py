# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class DongguanPipeline(object):
#     def __init__(self):
#         self.file = open("dongguan0401.json", 'w', encoding="utf-8")
#
#     def process_item(self, item, spider):
#
#         text = json.dumps(dict(item), ensure_ascii=False)
#         self.file.write(text + "\n")
#
#         return item
#
#     def close_spier(self, spider):
#         self.file.close()

class Sun2Pipeline(object):
    def process_item(self, item, spider):
        if spider.name == "sun2":
            item['content'] = self.handle_content(item['content'])

            text = json.dumps(dict(item), ensure_ascii=False)
            with open('sun2.json', 'a', encoding="utf-8") as f:
                f.write(text + '\n')

        return item

    def handle_content(self, contents):
        content = "".join(contents)

        str_map = {
            "\t": "",
            "\xa0": "",
            " ": "",
        }

        for i in str_map.keys():
            content = content.replace(i, str_map[i])

        return content
