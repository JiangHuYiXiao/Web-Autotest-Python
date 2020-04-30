# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/27 8:04
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
我们在进行自动化测试的很多时候，会遇到iframe框架的问题导致定位到的元素不能点击，这个时候我们需要先切换到iframe框架里面switch_to.frame()。
因为我们默认在主文档进行操作的default_content(),
如果有多个iframe嵌套，则我们需要一层一层切进去，切回来到主文档的时候只需要一次switch_to.default_content
切回到父iframe时候使用switch_to.parent_frame()
'''
# 示例1：登录126邮箱，并且发送邮件
from selenium import webdriver
import unittest
from time import sleep

class Test_126(unittest.TestCase):
    '''
    126邮箱操作类
    '''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://mail.126.com/')
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        print('用例执行start:')

    def tearDown(self):
        print('用例执行end:')

    def test_01login(self):
        '''登录126邮箱'''
        self.driver.find_element_by_xpath('//div[@id="lbNormal"]').click()
        sleep(1)
        # 定位iframe后切换iframe
        iframe_id = self.driver.find_elements_by_xpath('//iframe[starts-with(@id,"x-URS-iframe")]')
        self.driver.switch_to.frame(iframe_id[0])
        sleep(1)

        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys('jt19170920820')
        sleep(1)

        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys('jianghu123')
        sleep(1)
        self.driver.find_element_by_xpath('//a[@id="dologin"]').click()
        sleep(3)

    def test_02write(self):
        '''编写邮件'''
        # 切换到主文档，因为上面的登录用例的操作一直在iframe框架上
        self.driver.switch_to.default_content()
        sleep(1)
        self.driver.find_element_by_xpath('//span[()="写 信"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]').send_keys('1721906562@qq.com')
        sleep(1)
        self.driver.find_element_by_xpath('//input[contains(@id,"_subjectInput")]').send_keys('python_test')
        sleep(1)
        self.driver.find_element_by_xpath('//span[@class="nui-layer-close nui-close"]/b').click()
        # sleep(1)
        # 切换到iframe
        iframe_id1 = self.driver.find_elements_by_xpath('//iframe[@class="APP-editor-iframe"]')
        self.driver.switch_to.frame(iframe_id1[0])
        sleep(2)
        self.driver.find_element_by_xpath('/html/body').send_keys('test')
        sleep(1)
        # 切回到主文档
        self.driver.switch_to.default_content()
        send = self.driver.find_elements_by_xpath('//b[@class="js-component-icon nui-ico nui-ico-sent  nui-ico-sent-white  "]')
        send[0].click()


if __name__ == '__main__':
    unittest.main()