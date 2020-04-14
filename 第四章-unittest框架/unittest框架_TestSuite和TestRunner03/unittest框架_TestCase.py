# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 8:50
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('start')
    def test_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('http://www.baidu.com')
        sleep(1)
        driver.quit()
    def test_sogou(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('http://www.sogou.com')
        sleep(1)
        driver.quit()
    def tearDown(self):
        print('end')
if __name__ =='__main__':
    unittest.main()