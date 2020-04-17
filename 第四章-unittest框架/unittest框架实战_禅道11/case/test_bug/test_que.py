# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/17 15:54
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys

class Test_Que(unittest.TestCase):
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
        sleep(3)

    def test_addbug(self):
        pass

    def test_editbug(self):
        pass

