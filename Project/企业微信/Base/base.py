# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/8 11:08
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver

class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()