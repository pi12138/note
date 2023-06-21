from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# print("title:", driver.title)
text = driver.find_element_by_id('wrapper').text

print(text)
# 得到页面快照/截图
driver.save_screenshot('baidu_index.png')

# id="kw" 是百度的输入框，我们得到输入框的ui元素直接输入"大熊猫"
driver.find_element_by_id('kw').send_keys(u'大熊猫')
# id="su" 是百度的搜索按钮，click模拟点击
driver.find_element_by_id('su').click()

# 等待搜索结果
time.sleep(5)
driver.save_screenshot('大熊猫.png')

# 获取当前页面的所有cookie信息
print(driver.get_cookies())

# 模拟输入两个按键 ctrl + a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# ctrl + x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

# 重新输入内容,但是没有提交搜索
driver.find_element_by_id('kw').send_keys(u'航空母舰')
driver.save_screenshot('航空母舰01.png')

# 输入回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('航空母舰02.png')

# 清空输入框
driver.find_element_by_id('kw').clear()
driver.save_screenshot('清空01.png')

# 关闭浏览器
driver.quit()
