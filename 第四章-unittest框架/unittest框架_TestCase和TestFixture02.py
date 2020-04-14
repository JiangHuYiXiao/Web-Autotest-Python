# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 8:28
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
import unittest

class MyTestCase(unittest.TestCase):            # 必须继承unittest.TestCase
    def setUp(self):                            # 测试固件
        print('start')
    def test_baidu(self):                   # TestCase  测试用例必须是test开头
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('http://www.baidu.com')
        sleep(1)
        driver.quit()
    def tearDown(self):                            # 测试固件
        print('end')

if __name__ == '__main__':
    print(__name__)                 # __main__
    unittest.main()
