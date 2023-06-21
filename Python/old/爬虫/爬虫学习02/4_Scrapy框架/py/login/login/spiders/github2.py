"""
模拟登录2：
    利用 scrapy.FormRequest.from_response() 自动构造POST请求发送
"""
# -*- coding: utf-8 -*-
import scrapy


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        data = {
            "login": "1558255789@qq.com",
            "password": "zhou19981118"
        }

        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        with open('info2.html', 'w', encoding="utf-8") as f:
            f.write(response.body.decode())
