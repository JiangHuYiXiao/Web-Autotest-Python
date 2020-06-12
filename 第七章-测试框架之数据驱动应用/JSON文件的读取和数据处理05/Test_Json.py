# -*- coding:utf-8 -*-


# 使用json数据文件来进行驱动
from selenium import webdriver
import time,unittest,ddt

@ddt.ddt            # 声明
class Test(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.implicitly_wait(5)
    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
    @ddt.file_data('data.json')                 # 加载json文件
    @ddt.unpack
    def test_baidu(self,value):
        print(value)
        # shiji,yuqi = value.split('||')
        # print(shiji,yuqi)
        # self.driver.find_element_by_xpath('//input[@id="su"]').send_keys('')
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//input[@id="kw"]').click()
        # time.sleep(2)
        # self.assertIn(data,self.driver.page_source,'用例执行不通过')


if __name__ == '__main__':
    unittest.main()
