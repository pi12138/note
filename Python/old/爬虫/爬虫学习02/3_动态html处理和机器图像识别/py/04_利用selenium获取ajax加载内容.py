"""
使用selenium提取豆瓣电影剧情片数据
"""
from selenium import webdriver
from lxml import etree
import time
import json

class DouBanMovieSelenium:
    """
    豆瓣电影
    """
    def __init__(self):
        self.url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
        self.driver = webdriver.Chrome("F:\python自动化\chromedriver.exe")


    def load_page(self):
        """
        加载页面
        """
        self.driver.get(self.url)

        time.sleep(3)

        # 向下滚动1000像素
        js = "window.scrollBy(0, 1000)"
        # 滚动到当前页面底部
        # js = "window.scrollTo(0,document.body.scrollHeight)" 
        self.driver.execute_script(js)

        time.sleep(3)

        # self.driver.save_screenshot("1.jpg")
        # time.sleep(1)
    
        self.driver.execute_script(js)
        time.sleep(3)
        
        # self.driver.save_screenshot("2.jpg")

        self.parse_page(self.driver.page_source)


    def parse_page(self, html):
        """
        解析页面数据，提取页面内容
        html:加载到的html页面
        """
        text = etree.HTML(html)
        node_list = text.xpath('//div[contains(@class,"movie-list-item")]')
        # print(len(node_list))

        movie_list = []
        for node in node_list:
            title = node.xpath('.//div[@class="movie-name"]/span[1]/a')[0].text
            # rank =  node.xpath('.//div[@class="movie-name"]/span[3]')[0].text
            rank = node.xpath('.//span[@class="rank-num"]')[0].text
            rating = node.xpath(".//span[@class='rating_num']")[0].text

            movie_info = {
                'title': title,
                "rank": rank,
                "rating": rating,
            }
            movie_list.append(movie_info)

        self.write_info(movie_list)


    def write_info(self, movie):
        """
        将解析整理后的内容写到文件中
        movie:解析整理后的数据
        """
        with open("../text/doubanmovie2.json", 'w', encoding="utf-8") as f:
            f.write(json.dumps(movie, ensure_ascii=False))
        
        return "success"


    def close(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    db = DouBanMovieSelenium()
    db.load_page()
    db.close()