# -*- coding: utf-8 -*-
"""
1. 直接POST数据到登录提交的url地址
使用这种方式要开启 COOKIES_ENABLE
"""

import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        """
        重写start_requests，按照需要来发送请求
        """
        url = "http://www.renren.com/PLogin.do"
        data = {
            "email": "13193820382",
            "password": "zhou19981118",
        }

        yield scrapy.FormRequest(
            url=url,
            formdata=data,
            callback=self.parse_page
        )

    def parse_page(self, response):
        """
        处理登录后的response文件
        """
        with open("./file/renren1.html", 'w', encoding="utf-8") as f:
            f.write(response.body.decode())
