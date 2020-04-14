# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 15:52
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
import unittest


# 在本测试TestCase执行，是按照ascii码顺序执行的，所以肯定是先执行baidu2，后执行sogou2
class MyTestCase2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print('start')
    def test_sogou2(self):
        self.driver.get('http://www.sogou.com')
        sleep(1)
    def test_baidu2(self):
        self.driver.get('http://www.baidu.com')
        sleep(1)
    def tearDown(self):
        self.driver.quit()
        print('end')
if __name__ =='__main__':
    unittest.main()
