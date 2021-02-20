# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/9 15:44
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
使用driver.get_cookies()获取当前页面的所有cookie
'''

import shelve,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_cookies():
    def setup(self):
        chrome_options = Options()
        chrome_options.debugger_address = '127.0.0.1:9666'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def test_cookies(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')   #
        db = shelve.open('cookies')                     # 打开并且创建三个以cookies开头的文件
        # db['cookie'] = self.driver.get_cookies()       # 先使用

        # 后使用
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')

            self.driver.add_cookie(cookie)                                          #
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')  #
        time.sleep(5)
        db.close()

    def teardown(self):
        self.driver.quit()
