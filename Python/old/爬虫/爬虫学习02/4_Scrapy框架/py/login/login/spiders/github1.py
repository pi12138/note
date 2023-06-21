"""
模拟登陆1：
    使用 scrapy.FormRequest() 手动构造POST请求进行模拟登录
"""
# -*- coding: utf-8 -*-
import scrapy


class Github1Spider(scrapy.Spider):
    name = 'github1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):

        form_data = {
            "commit": response.xpath('//input[@name="commit"]/@value').extract_first(),
            "utf8": response.xpath('//input[@name="utf8"]/@value').extract_first(),
            "authenticity_token": response.xpath('//input[@name="authenticity_token"]/@value').extract_first(),
            "login": "1558255789@qq.com",
            "password": "zhou19981118",
            "webauthn-support": response.xpath('//input[@name="webauthn-support"]/@value').extract_first()
        }

        yield scrapy.FormRequest(
            url="https://github.com/session",
            formdata=form_data,
            callback=self.parse_page,
        )

    def parse_page(self, response):
        """处理模拟登录后的页面"""
        with open('info1.html', 'w', encoding="utf-8") as f:
            f.write(response.body.decode())
