# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/968608156/profile']

    cookies = {
        "anonymid": "jo6sr79k40ag06", " _r01_": "1",
        " jebe_key": "677bb307-0e02-4841-bef6-440071dd690f%7C7471263abebbaff7e175aa883e8f567c%7C1541573100604%7C1%7C1541573369733",
        " __utma": "151146938.1258973640.1541599502.1541599502.1541599502.1",
        " __utmz": "151146938.1541599502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/968602505/profile",
        " ln_uact": "13193820382", " ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif", " depovince": "HEN",
        " JSESSIONID": "abcr38wR18rn_6n56mMNw", " ick_login": "6d5bc661-78e1-44a8-bbe0-59b11c843b1e",
        " first_login_flag": "1", " jebecookies": "8b63079c-7bd7-4888-b125-5de6300b25a6|||||",
        " _de": "808C2653025A488A50C4B45F09ACB784", " p": "9733afd56c1935ab85b93e213ef268986",
        " t": "98d86325c0c1d4447aa8f613c028cd9b6", " societyguester": "98d86325c0c1d4447aa8f613c028cd9b6",
        " id": "968608156", " xnsid": "1960178b", " ver": "7.0", " loginfrom": "null", " wp_fold": "0",
        " jebe_key": "677bb307-0e02-4841-bef6-440071dd690f%7Cf32e82e144a38fbd54204d837fb67154%7C1554355395119%7C1%7C1554355393791",
    }

    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], cookies=self.cookies, callback=self.parse_page)

    def parse_page(self, response):
        with open("./file/renren3.html", "w", encoding="utf-8") as f:
            f.write(response.body.decode())

    def parse(self, response):
        pass
