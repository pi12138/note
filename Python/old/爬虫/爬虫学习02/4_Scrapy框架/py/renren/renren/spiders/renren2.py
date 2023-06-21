# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    def parse(self, response):
        """
        通过登录页面的response，发送POST数据
        """
        data = {
            "email": "13193820382",
            "password": "zhou19981118",
        }

        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        """
        登录成功后，进入个人主页
        """
        url = "http://www.renren.com/968608156/profile"
        yield scrapy.Request(url, callback=self.parse_profile)

    def parse_profile(self, response):
        """
        个人主页写入文件
        """
        with open("./file/renren2.html", 'w', encoding="utf-8") as f:
            f.write(response.body.decode())
