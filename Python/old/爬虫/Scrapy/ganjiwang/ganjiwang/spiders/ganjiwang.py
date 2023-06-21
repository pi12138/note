'''
爬取赶集网杭州租房信息的一个小案例
不能过多操作，网站会有反馈
'''
import scrapy


class house_informationspider(scrapy.Spider):
    name = 'ganjiwanghouse_information'
    start_urls = ["http://hz.ganji.com/fang1/p4/"]

    def parse(self, response):
        # print("response:",response)
        title_info = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        # print(title_info)
        price_info = response.xpath("//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div/span[@class='num']/text()").extract()

        # 写入文件
        with open(r'赶集网租房信息.txt', 'w', encoding = 'utf-8') as f:
            for t, p in zip(title_info, price_info):
                f.write(t + ":" + p + '\n')
            # with open('赶集网租房信息.txt', 'w', encoding='utf-8') as f:
                # f.write()
