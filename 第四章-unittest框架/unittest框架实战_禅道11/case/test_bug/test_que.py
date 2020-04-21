# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/17 15:54
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys
from untils.duan_in import duan_in
# from untils.log_cn import make_report

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
    # @unittest.expectedFailure
    # 登录
    # @unittest.expectedFailure
    def test_00login(self):
        # print('111')
        self.driver.find_element_by_xpath('//input[@id="account"]').send_keys('admin')
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('jianghu@123')
        self.driver.find_element_by_xpath('//button[@id="submit"]').click()
        sleep(1)
        # self.assertIn('我的地盘211',self.driver.page_source,'登录失败')

        # 调用断言方法判断是否登录成功
        duan_in('我的地盘',self.driver.page_source,'登录用例')
        sleep(3)

    def test_01addbug(self):
        self.driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="subNavbar"]/ul/li[1]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainMenu"]/div[3]/a[3]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="openedBuild_chosen"]/ul').click()
        self.driver.find_element_by_xpath('//*[@id="openedBuild_chosen"]/div/ul/li[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys('创建工作日历报错')
        self.driver.execute_script("scroll(0,600)")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        sleep(2)

    def test_editbug(self):
        self.driver.find_element_by_xpath('//*[@id="bugList"]/tbody/tr[1]/td[11]/a[3]/i').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="module_chosen"]/a/span').click()
        self.driver.find_element_by_xpath('//*[@id="module_chosen"]/div/ul/li[2]').click()
        sleep(1)
        self.driver.execute_script("scroll(0,600)")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        sleep(1)



if __name__ =='__main__':
    unittest.main()