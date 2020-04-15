# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 8:14
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、assertEqual(self, first, second, msg=None)      对比预期结果和实际结果是否相等,msg为可选参数，用于定义测试失败时打印的信息。
# 2、assertNotEqual(self, first, second, msg=None)   对比预期结果和实际结果是否不相等,msg为可选参数，用于定义测试失败时打印的信息。
# 3、assertTrue(self, expr, msg=None):               用于判断表达式expr是True吗,msg为可选参数，用于定义测试失败时打印的信息。
# 4、assertFalse(self, expr, msg=None):              用于判断表达式expr是False吗,msg为可选参数，用于定义测试失败时打印的信息。
# 5、assertIs(self, expr1, expr2, msg=None):         用于判断表达式expr1和expr2是否是同一个对象
# 6、assertIsNot(self, expr1, expr2, msg=None):      用于判断表达式expr1和expr2是否不是同一个对象
# 7、assertIsNone(self, obj, msg=None):              用于判断obj是是None
# 8、assertIsNotNone(self, obj, msg=None):           用于判断obj是不是None
# 9、assertIn(arg1, arg2, msg=None)	                 验证arg1是arg2的子串，不是则fail
# 10、assertNotIn(arg1, arg2, msg=None)	             验证arg1不是arg2的子串，是则fail
# 11、assertIsInstance(obj, cls, msg=None)	         验证obj是cls的实例，不是则fail
# 12、assertNotIsInstance(obj, cls, msg=None)	     验证obj不是cls的实例，是则fail

# 用例运行的结果有四种状态，{成功:.,错误:E，失败:F，跳过:S}
import unittest
from selenium import webdriver
from time import sleep

class TestCase_baidu(unittest.TestCase):

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
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('keep up')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('keep up_百度搜索',self.driver.title,'不相等')
        self.assertIn('keep up',self.driver.page_source,'不包含')

    def test_baidu_chinese(self):
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('鬼吹灯')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('鬼吹灯_百度搜索', self.driver.title, '不相等')
        # self.assertEqual('123', self.driver.title, '不相等')
        self.assertIn('沙子',self.driver.page_source,'不包含')

    def test_baidu_pinyin(self):
        self.driver.find_element_by_xpath('//input[@id = "kw"]').send_keys('laohu')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        # self.assertEqual('laohu_百度搜索', self.driver.title, '不相等')
        self.assertIn('laohu',self.driver.page_source,'不包含')

if __name__ == '__main__':
    unittest.main()
