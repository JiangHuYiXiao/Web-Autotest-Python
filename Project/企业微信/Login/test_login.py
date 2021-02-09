# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/8 11:16
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

import time
from selenium import webdriver
# from Base.base import Base
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions


class Test_login():
    def setup(self):
        options = Options()
        options.debugger_address='127.0.0.1:9666'
        self.driver = webdriver.Chrome(options=options)
        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()

    def test_login(self):
        # self.driver.get('https://work.weixin.qq.com')
        # self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]')
        # expected_conditions.visibility_of_element_located(self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]'))
        # self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]').click()
        expected_conditions.visibility_of_element_located(self.driver.find_element_by_xpath('//a[@id="menu_contacts"]'))
        self.driver.find_element_by_xpath('//a[@id="menu_contacts"]').click()
        time.sleep(5)
