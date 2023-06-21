'''
通过WebDriver操作百度进行查找
'''

from selenium import webdriver
import time
# 通过Keys模拟键盘
from selenium.webdriver.common.keys import Keys
# 操作那个浏览器就对哪个浏览器创建一个实例
# 自动按照环境变量查找相应的浏览器
# 如果浏览器没有在相应的环境变量中，需要指定浏览器位置
driver = webdriver.PhantomJS()

driver.get('https://www.baidu.com')

print("title:{0}".format(driver.title))