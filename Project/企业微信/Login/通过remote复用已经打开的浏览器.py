# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/8 11:16
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
1、首先需要把chrome浏览器的应用路径放入环境变量：C:\Users\Administrator\AppData\Local\Google\Chrome\Application。
2、关闭所有的浏览器进程。
3、cmd命令窗口运行命令：chrome --remote-debugging-port=9666  端口自己随便取一个没有使用的。
'''


import time
from selenium import webdriver
# from Base.base import Base
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions


class Test_login():
    def setup(self):
        chrome_options = Options()
        chrome_options.debugger_address='127.0.0.1:9666'
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        # self.driver.get('https://work.weixin.qq.com')
        # self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]')
        # expected_conditions.visibility_of_element_located(self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]'))
        # self.driver.find_element_by_xpath('//a[@class="index_top_operation_loginBtn"]').click()
        expected_conditions.visibility_of_element_located(self.driver.find_element_by_xpath('//a[@id="menu_contacts"]'))
        self.driver.find_element_by_xpath('//a[@id="menu_contacts"]').click()
        time.sleep(5)
