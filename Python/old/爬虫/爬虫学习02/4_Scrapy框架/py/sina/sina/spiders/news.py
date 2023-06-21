"""
失败案例，
"""
#
# # -*- coding: utf-8 -*-
# import scrapy
# from ..items import SinaItem
# import os
#
#
# class NewsSpider(scrapy.Spider):
#     name = 'news'
#     allowed_domains = ['news.sina.com.cn']
#     start_urls = ['https://news.sina.com.cn/guide/']
#
#     def parse(self, response):
#         # pass
#         divs = response.xpath('//div[@id="tab01"]/div')
#
#         for div in divs[:-1]:
#             item = SinaItem()
#
#             item['first_title'] = div.xpath('./h3/a/text()').extract()[0]
#             item['first_url'] = div.xpath('./h3/a/@href').extract()[0]
#
#             floder_path1 = './data/'+item['first_title']
#             if os.path.exists(floder_path1):
#                 pass
#             else:
#                 os.mkdir(floder_path1)
#
#             lis = div.xpath('./ul/li')
#
#             for li in lis:
#                 item = SinaItem()
#
#                 item['second_title'] = li.xpath('./a/text()').extract()[0]
#                 item['second_url'] = li.xpath('./a/@href').extract()[0]
#
#                 floder_path2 = floder_path1 + "/" + item['second_title']
#                 if os.path.exists(floder_path2):
#                     pass
#                 else:
#                     os.mkdir(floder_path2)
#
#                 info = {
#                     "second_url": item['second_url'],
#                     "file_path": floder_path2 + "/",
#                     }
#
#                 yield scrapy.Request(url=item['second_url'], callback=self.parse_second_page, meta=info)
#
#     def parse_second_page(self, response):
#         second_url = response.meta['second_url']
#         file_path = response.meta['file_path']
#         hrefs = response.xpath('//a[contains(@href, "{}")]'.format(second_url)).extract()
#
#         for href in hrefs:
#             yield scrapy.Request(url=href, callback=self.parse_third_page, meta={'file_path': file_path})
#
#     def parse_third_page(self, response):
#         file_path = response.meta['file_path']
#
#         item = SinaItem()
#
#         title = response.xpath('//h1[@class="main-title"]').extract()[0]
#         content_list = response.xpath('//div[@class="article-content-left"]/div[@class="article"]//p[@class]').extract()
#
#         content = ""
#         for i in content_list:
#             content += i
#
#         item['third_title'] = title
#         item['third_content'] = content
#         item['file_path'] = file_path
#
#         yield item
#
