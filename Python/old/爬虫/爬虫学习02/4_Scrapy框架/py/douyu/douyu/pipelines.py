# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


# class DouyuPipeline(object):
#     def process_item(self, item, spider):
#         return item


class DouyuPipeline(ImagesPipeline):
    IMAGE_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item['image_url']

        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，则放入 image_path 里
        image_path = [x['path'] for ok, x in result if ok]

        os.rename(self.IMAGE_STORE+image_path[0], self.IMAGE_STORE+item['name']+'.jpg')
        item['image_path'] = self.IMAGE_STORE + item['name']

        return item

    # get_media_requests的作用就是为每一个图片链接生成一个Request对象，
    # 这个方法的输出将作为item_completed的输入中的results，
    # result是一个包含tuple的容器,容器中每个元组包含两个值，每个元组包括(success, image_info_or_failure)。
    # 如果success=true，imageinfoor_failure是一个字典，包括url/path/checksum三个key。
