# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/26 9:25
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 业务场景：在一个用例类中，不同的用例连续执行，需要打开不同的窗口
import unittest,selenium,time
from selenium import webdriver

class Test_Baidu_Handles(unittest.TestCase):
    '''
    百度多窗口测试类
    '''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://news.baidu.com/')

    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        self.driver.quit()

    def hands_check(self,hands,driver,duanyan):
        '''
        多窗口操作hands和断言方法
        :param hands:
        :param driver:
        :param duanyan:
        :return:
        '''
        try:
            self.assertEqual(duanyan, driver.title, '预期与实际不相等')
        except AssertionError as e:
            self.assertEqual(duanyan, driver.title, '预期与实际不相等')
        finally:
            # 不管如何先要关闭当前页面，然后切回到最初的页面，这样下面的用例才能继续在最初的窗口上寻找元素，进行操作
            for i in range(len(hands)):
                if i == len(hands)-1:
                    break
                else:
                    self.driver.close()
                    self.driver.switch_to.window(hands[len(hands)-i-2])

    def setUp(self):
        print('用例执行：start')

    def tearDown(self):
        print('用例执行：end')

    def test_01(self):
        '''热点要闻测试'''
        self.driver.find_element_by_xpath('//div[@class="hotnews"]/ul/li/strong/a').click()
        time.sleep(2)
        hands = self.driver.window_handles
        # current_handle = self.driver.current_window_handle
        # print(hands,current_handle,hands[0],hands[1])
        # 切换到新开的窗口
        self.driver.switch_to.window(hands[1])
        # 异常处理
        self.hands_check(hands,self.driver,'陕西之行  习近平为如期实现全面脱贫注入新动力--时政--人民网')
        time.sleep(2)



    def test_02(self):
        '''广州要闻测试'''
        self.driver.execute_script('scroll(0,900)')
        time.sleep(1)
        self.driver.find_element_by_xpath('//ul[@id="localnews-focus"]/li/a').click()
        time.sleep(2)
        hands = self.driver.window_handles
        # current_hands = self.driver.current_window_handle
        # print(hands,current_hands)
        self.driver.switch_to.window(hands[1])
        # 异常处理
        self.hands_check(hands,self.driver,'微信预约就可核酸检测！周六广州红会医院外排起了长队_南方plus_南方+')

if __name__ == '__main__':
    unittest.main()