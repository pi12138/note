"""
本来想爬取前10页内容，结果发现第一页都挺多的，就只爬取了第一页
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time


class DouYuLOL:
    """
    斗鱼lol类
    """
    def __init__(self):
        self.url = "https://www.douyu.com/g_LOL"
        self.anchor = 0
        self.audience = 0
        self.driver = webdriver.Chrome("F:\python自动化\chromedriver.exe")
     

    def load_page(self):
        """加载页面"""
        self.driver.get(self.url)
        time.sleep(3)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        user_list = soup.find_all("h2", {"class": "DyListCover-user"})
        hot_list = soup.find_all("span", {"class":"DyListCover-hot"})

        if len(user_list) == len(hot_list):
            for user, hot in zip(user_list, hot_list):
                # print("主播:{0}\t热度:{1}".format(user.get_text(), hot.get_text()))
                print("主播:{0}\t热度:{1}".format(user.text, hot.text))
                num = float(hot.text[:-1])
                self.audience += num
        else:
            print("error")

        time.sleep(3)    

    def close(self):
        print("总热度：{}".format(self.audience))
        self.driver.quit()

if __name__ == "__main__":

    douyu = DouYuLOL()
    douyu.load_page()
    douyu.close()
