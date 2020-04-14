# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 16:27
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest
from selenium import webdriver
from time import sleep

class TestCase11(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()
        print('start')
    def test_baidu1(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)

    def test_sogou1(self):
        self.driver.get('http://www.sogou.com')
        sleep(1)
    def tearDown(self):
        self.driver.quit()
        print('end')

if __name__ =='__main__':
    unittest.main()