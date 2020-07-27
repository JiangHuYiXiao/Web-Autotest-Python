# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/27 8:31
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import time,unittest
from selenium import webdriver

class Baidu_Search(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com/')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        pass

    def test_search(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys('胡锡进')
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        time.sleep(2)
        self.assertEqual('胡锡进_百度搜索',self.driver.title)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


