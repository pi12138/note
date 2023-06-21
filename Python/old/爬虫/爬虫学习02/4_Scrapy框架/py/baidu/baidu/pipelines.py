# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


# class BaiduPipeline(object):
#     def process_item(self, item, spider):
#         return item


class BaiduTiebaPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_list = item['image_list']
        if image_list:
            for image in image_list:
                item['name'] = image[-10:]
                yield scrapy.Request(url=image)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if image_path:
            os.rename(self.IMAGES_STORE+image_path[0], self.IMAGES_STORE+item['name']+'.jpg')
            item['image_path'] = self.IMAGES_STORE + item['name']

        return item
