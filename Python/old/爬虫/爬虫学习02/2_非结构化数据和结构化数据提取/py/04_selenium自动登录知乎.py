"""
存在问题

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ZhiHuLogin:
    """
    使用selenium登录知乎
    """
    def __init__(self):
        self.url = "https://www.zhihu.com/signup?next=%2F"
        self.driver = webdriver.Chrome(r"F:\python自动化\chromedriver.exe")
        self.username = "18790065681"
        self.password = "zhou19981118"    

    def login(self):
        """
        登录知乎
        """
        self.driver.get(self.url)
        login_btn = self.driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span')
        login_btn.click()

        time.sleep(2)   

        phone_number_login = self.driver.find_element_by_xpath('//button[@class="Button Login-switchType Button--plain"]')
        phone_number_login.click()
        
        time.sleep(1)

        phone_input = self.driver.find_element_by_xpath('//input[@name="username"]')
        verification_input = self.driver.find_element_by_xpath('//input[@name="digits"]')
        verification_code_btn = self.driver.find_element_by_xpath('//button[@class="Button CountingDownButton SignFlow-smsInputButton Button--plain"]')
        submit_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')

        time.sleep(1)

        phone_input.send_keys(self.username, Keys.ARROW_DOWN)

        verification_code_btn.click()

        verification = int(input("请输入验证码:"))
        
        verification_input.send_keys(verification, Keys.ARROW_DOWN)

        time.sleep(1)

        submit_btn.submit()

        # username_input = self.driver.find_element_by_xpath('//input[@name="username"]')
        # password_input = self.driver.find_element_by_xpath('//input[@name="password"]')
        # submit_btn = self.driver.find_element_by_xpath('//button[@type="submit"]')
        # username_input.send_keys(self.username, Keys.ARROW_DOWN)
        # time.sleep(2)
        # password_input.send_keys(self.password, Keys.ARROW_DOWN)
        # time.sleep(1)
        # submit_btn.submit()

        time.sleep(3)

        cookies = self.driver.get_cookies()

        print(cookies)

    def close(self):
        """
        关闭浏览器对象
        """
        self.driver.close()


if __name__ == "__main__":
    zh = ZhiHuLogin()
    zh.login()