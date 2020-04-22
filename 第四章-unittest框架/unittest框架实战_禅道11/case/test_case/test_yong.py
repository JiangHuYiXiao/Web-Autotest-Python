# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/17 8:30
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest
from untils.duan_in import duan_in
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
        # 调用自定义的断言方法，注释自带的
        # self.assertIn('我的地盘',self.driver.page_source,'登录失败')
        sleep(3)
        duan_in(self.driver, '我的地盘', self.driver.page_source, '登录用例')

    # 添加用例
    def test_01addcase(self):
        self.driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="subNavbar"]/ul/li[2]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainMenu"]/div[3]/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('创建工作日历')
        sleep(1)
        self.driver.find_element_by_xpath('//button[@id="submit"]').click()
        sleep(3)
        duan_in(self.driver, '创建工作日历', self.driver.page_source, '创建工作日历用例')
    # 编辑用例
    def test_02editcase(self):
        self.driver.find_element_by_xpath('//*[@id="caseList"]/tbody/tr/td[13]/a[3]/i').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pri_chosen"]/a/span').click()

        self.driver.find_element_by_xpath('//*[@id="pri_chosen"]/div/ul/li[3]').click()
        self.driver.execute_script("scroll(0,1000)")
        sleep(1)
        self.driver.find_element_by_xpath('//button[@id="submit"]').click()
        sleep(2)
        duan_in(self.driver, '创建工作日历', self.driver.page_source, '修改工作日历用例')

if __name__ == '__main__':
    unittest.main()