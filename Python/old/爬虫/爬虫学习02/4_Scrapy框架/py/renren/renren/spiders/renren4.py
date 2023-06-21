"""
重写 start_requests() 方法，发送第一个请求，
使用 cookie 模拟登录
"""
# -*- coding: utf-8 -*-
import scrapy
import re


class Renren4Spider(scrapy.Spider):
    name = 'renren4'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/968608156/profile']

    def start_requests(self):
        cookie = "anonymid=jo6sr79k40ag06; _r01_=1; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7C7471263abebbaff7e175aa883e8f567c%7C1541573100604%7C1%7C1541573369733; __utma=151146938.1258973640.1541599502.1541599502.1541599502.1; __utmz=151146938.1541599502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/968602505/profile; ln_uact=13193820382; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; _de=808C2653025A488A50C4B45F09ACB784; depovince=HEN; jebecookies=83b4ba29-dc11-4de7-a380-23a783f40d18|||||; JSESSIONID=abcFe4LGRJaHQ-LDTJZOw; ick_login=f802c998-7e62-4965-a070-6e01bfd271ac; p=ca6c70a9492e862dd51dd4d1fd4b48ab6; first_login_flag=1; t=ee8acb55a72195573aa8b105ea7acdb46; societyguester=ee8acb55a72195573aa8b105ea7acdb46; id=968608156; xnsid=cc70fd6c; ver=7.0; loginfrom=null; wp_fold=0; XNESSESSIONID=ac0943c25dcc; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7Cf32e82e144a38fbd54204d837fb67154%7C1555643556029%7C1%7C1555643547997"

        # 处理cookie字符串，使其成为字典形式
        # 此处使用字典推导式
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}

        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        # 查找个人页面内容，看看是否成功进入个人主页
        # 若查找到内容则代表使用cookie登录成功
        print(re.findall("周", response.body.decode()))
