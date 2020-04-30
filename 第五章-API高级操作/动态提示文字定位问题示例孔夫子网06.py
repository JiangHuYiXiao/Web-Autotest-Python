# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/30 8:27
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
关于动态提示信息的定位
'''
from time import sleep
from selenium import webdriver
import unittest

class Test_Kong(unittest.TestCase):
    '''孔夫子旧书网操作类'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()
        self.driver.get('https://login.kongfz.com/')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        print('用例执行start：')

    def tearDown(self):
        print('用例执行end：')

    def test_01username_error(self):
        '''用户名不存在测试用例'''
        self.driver.find_element_by_xpath('//input[@id="username"]').send_keys('jinaghuyixiao1')
        sleep(1)
        self.driver.find_element_by_xpath('//input[@id="password"]').send_keys('jianghu1234')
        sleep(10)               # 等待手工输入验证码
        self.driver.find_element_by_xpath('//input[@class="login_submit btn_red_h40"]').click()
        sleep(3)
        # 获取用户名不存在的提示信息
        username_error_info = self.driver.find_element_by_xpath('//label[@id="username-error"]').text
        print(username_error_info)


if __name__ == '__main__':
    unittest.main()

'''
用例执行start：
用户名不存在
用例执行end：
'''