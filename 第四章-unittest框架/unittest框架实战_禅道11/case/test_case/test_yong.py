# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/17 8:30
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest
class Test_Yong(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://172.20.49.38:92/zentao/')
        sleep(2)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        print('用例执行：start')

    def tearDown(self):
        print('用例执行：end')
    @unittest.expectedFailure
    # 登录
    def test_00login(self):
        # print('111')
        self.driver.find_element_by_xpath('//input[@id="account"]').send_keys('admin')
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('jianghu@123')
        self.driver.find_element_by_xpath('//button[@id="submit"]').click()
        sleep(1)
        self.assertIn('我的地盘',self.driver.page_source,'登录失败')
        sleep(1)
    # 添加用例
    def test_addcase(self):
        self.driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click()
        self.driver.find_element_by_xpath()
        sleep(4)
        self.assertEqual(1,1)
    # 编辑用例
    # def test_editcase(self):
    #     pass

if __name__ == '__main__':
    unittest.main()