# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 8:14
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 给类或者方法加上注释后，在报告中的用例名称后就会有
# 用例运行的结果有四种状态，{成功:.,错误:E，失败:F，跳过:S}
import unittest
from selenium import webdriver
from time import sleep

class TestCase_baidu(unittest.TestCase):
    '''百度搜索用例集合'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        self.driver.get('http://www.baidu.com')
        sleep(2)

    def tearDown(self):
        print('一条用例执行完毕')

    def test_baidu_english(self):
        ''' 英文搜索'''
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('keep up')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('keep up_百度搜索',self.driver.title,'不相等')
        self.assertIn('keep up',self.driver.page_source,'不包含')

    def test_baidu_chinese(self):
        ''' 中文搜索'''
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('鬼吹灯')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('鬼吹灯_百度搜索', self.driver.title, '不相等')
        # self.assertEqual('123', self.driver.title, '不相等')
        self.assertIn('沙子',self.driver.page_source,'不包含')

    def test_baidu_pinyin(self):
        ''' 拼音搜索'''
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('laohu')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('laohu_百度搜索', self.driver.title, '不相等')
        self.assertIn('laohu',self.driver.page_source,'不包含')

if __name__ == '__main__':
    unittest.main()
