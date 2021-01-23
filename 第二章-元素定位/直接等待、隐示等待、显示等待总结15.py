# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/1/23 10:41
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_time():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐示等待
        # self.driver.implicitly_wait(5)    会应用所有的find方法
    def setup_method(self):
        print('************测试开始************')
    def test_time(self):
        self.driver.get('http://www.baidu.com/')
        # 显示等待方式1
        # WebDriverWait(self.driver, 5, 0.5).until(
        #     lambda x: x.find_element_by_xpath('//input[@id="kw"]'))
        # 显示等待方式2：
        expected_conditions.visibility_of_element_located(self.driver.find_element_by_xpath('//input[@id="kw1"]'))
        self.driver.find_element_by_xpath('//input[@id="kw"]').clear()
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('嬴政')
        # 直接等待
        # time.sleep(2)
        WebDriverWait(self.driver, 5, 0.5).until(
            lambda x: x.find_element_by_xpath('//input[@id="su"]'))
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        # 直接等待
        # time.sleep(2)

    def teardown_method(self):
        print('************测试结束************')

    def teardown_class(self):
        self.driver.quit()
