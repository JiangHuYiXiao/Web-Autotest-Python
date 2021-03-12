# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/26 11:10
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Project.企业微信.PageObject实战1.PO.index import Index


class Test_work():
    def setup(self):
        self.index = Index()
        # chrome_options = Options()
        # chrome_options.debugger_address = '127.0.0.1:9666'
        # self._driver = webdriver.Chrome(options=chrome_options)  # options='127.0.0.1:9222'
        # self._driver.implicitly_wait(5)
        # self._driver.maximize_window()
        print('start')

    def teardown(self):
        print('end')
        # self.quit()
    def test_work_weixin(self):
        self.index.click_login().click_register().send_content()
        # self.index.click_register()
