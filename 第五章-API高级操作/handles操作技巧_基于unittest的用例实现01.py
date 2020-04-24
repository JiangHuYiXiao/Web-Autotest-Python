# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/23 8:21
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
        self.driver.quit()

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
        try:
            self.assertEqual('1习近平给参与“东方红一号”任务的老科学家回信强调 敢于战胜一切艰难险阻 勇于攀登航天科技高峰-新华网)',self.driver.title,'预期与实际不相等')
        except AssertionError as e:
            print('预期和实际不相等，用例执行不通过')
        finally:
            # 不管如何切回到最初的页面，这样下面的用例才能继续在最初的窗口上寻找元素，进行操作
            self.driver.close()
            self.driver.switch_to.window(hands[0])
            self.assertEqual('1习近平给参与“东方红一号”任务的老科学家回信强调 敢于战胜一切艰难险阻 勇于攀登航天科技高峰-新华网)', self.driver.title,'预期与实际不相等')


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
        try:
            self.assertEqual('打造议事平台，广州法律服务集聚区成立“大党委”_南方plus_南方+', self.driver.title, '预期与实际不相等')
        except AssertionError as e:
            print('预期和实际不相等，用例执行不通过')
            self.assertEqual('打造议事平台，广州法律服务集聚区成立“大党委”_南方plus_南方+', self.driver.title, '预期与实际不相等')
        finally:

            self.driver.close()


if __name__ == '__main__':
    unittest.main()