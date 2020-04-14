# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 19:59
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 测试套件不仅有setUp()、tearDown(),这里的语句每次执行一条用例都会执行一次
# 还有setUpClass(),tearDownClass()，这里的语句每一个类，只执行一次


import unittest
from selenium import webdriver
from time import sleep

class TestCase_baidu(unittest.TestCase):
    @classmethod
    def setUpClass(self):           # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    @classmethod
    def tearDownClass(self):        # 关闭浏览器
        self.driver.quit()

    def setUp(self):
        self.driver.get('http://www.baidu.com/')
        sleep(2)

    def tearDown(self):
        print('一条用例执行完毕')

    def test_baidu_chinese(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('盗墓笔记')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        self.assertEqual('盗墓笔记_百度搜索',self.driver.title)
        # 断言后面一般不加任何语句，因为只要断言失败则这些语句都不会执行

    def test_baidu_english(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('demon')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        self.assertEqual('demon_百度搜索',self.driver.title)
        # 断言后面一般不加任何语句，因为只要断言失败则这些语句都不会执行

    def test_baidu_pinyin(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('laohu')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        self.assertEqual('laohu_百度搜索',self.driver.title)
        # 断言后面一般不加任何语句，因为只要断言失败则这些语句都不会执行

if __name__ == '__main__':
    # print(__name__)
    unittest.main()
