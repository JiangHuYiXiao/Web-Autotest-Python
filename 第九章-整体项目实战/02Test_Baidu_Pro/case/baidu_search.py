# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/27 8:31
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import time,unittest,ddt
from selenium import webdriver
from baidu_tools.ReadExcel import Parse_Excel
excel_path = './../data/baidu_test_data.xlsx'
sheetname = 'baidu_sou'
excel = Parse_Excel(excel_path,sheetname)

@ddt.ddt
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

    @ddt.data( * excel.getDataFromSheet())
    def test_search(self,data):
        print(data)
        self.driver.find_element_by_xpath('//input[@id="kw"]').clear()
        self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys(data[0])
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        time.sleep(2)
        self.assertEqual(data[1]+'_百度搜索',self.driver.title)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


