# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/28 7:47
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
有的时候我们在定位时候会遇到各种各样的问题导致我们明明能够定位的元素怎么也定位不了，这个时候我们需要变通处理
应用我们之前的八种定位方法，这里这个sina邮箱登录写信发送就遇到这种情况，
这里使用的办法是应用之前学的xpath轴，/following::,选择当前节点之后的所有子节点来进行定位
'''
import unittest,time
from selenium import webdriver
class Test_Sina(unittest.TestCase):
    '''sina邮箱操作类'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        print('用例执行start：')

    def tearDown(self):
        print('用例执行end：')
    # @unittest.expectedFailure
    def test_01login_sina(self):
        '''sina邮箱登录用例'''
        self.driver.find_element_by_xpath('//input[@id="freename"]').send_keys('jianghupython@sina.com')
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="freepassword"]').send_keys('jianghu123')
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="store1"]').click()
        self.driver.find_element_by_xpath('//input[@id="ssl1"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="freeMailbox"]/div[7]/div/a').click()
        time.sleep(3)

    def test_02write_email(self):
        '''sina邮箱写信发送用例'''
        # 直接定位(有时候定位不了)
        # self.driver.find_element_by_xpath('//li[@class="wrWriteBtn"]/a').click()
        # 间接定位
        # 以后很多时候定位不到这样去调试，一步步进行
        # yx = self.driver.find_elements_by_xpath('//div[@class="wui-PaneSinaMail"]//following::div[@class="wui-PaneSinaMail_bgr"]')
        # print(len(yx))
        # div[2]div/div/div/ul/li/a

        # 复杂版
        # su = self.driver.find_elements_by_xpath('//div[@class="wui-PaneSinaMail"]//following::div[@class="wui-PaneSinaMail_bgr"]/div[5]/div[2]/div/div/div/ul/li/a')
        # print(len(su),su[0].get_attribute('class'))
        # su[0].click()
# V1
        # 简化版
        # 写信
        # str = '//div[@class="wui-PaneSinaMail"]//following::'
        # self.driver.find_element_by_xpath(str+'li[@class="wrWriteBtn"]/a').click()
        # time.sleep(2)
        # # 收件人
        # self.driver.find_element_by_xpath('//tr[@class="fwReceiver"]/td/ul/li/input').send_keys('1721906562@qq.com')
        # time.sleep(1)
        # # 主题
        # self.driver.find_element_by_xpath('//input[@name="subj"]').send_keys('python test')
        # time.sleep(2)
        # # 切换iframe
        # iframe_edit = self.driver.find_elements_by_xpath('//div[@id="SinaEditor"]/iframe')
        # self.driver.switch_to.frame(iframe_edit[0])
        # time.sleep(1)
        # # 内容
        # self.driver.find_element_by_xpath('/html/body').send_keys('测试')
        # time.sleep(2)
        # # 回到主文档
        # self.driver.switch_to.default_content()
        #
        # # 发送
        # self.driver.find_element_by_xpath('//*[@id="panel_main"]/div[1]/span/span[1]/a/i[2]').click()
        # time.sleep(2)
# V2
        str = '//div[@class="wui-PaneSinaMail"]//following::'
        self.driver.find_element_by_xpath(str+'li[@class="wrWriteBtn"]/a').click()
        time.sleep(2)
        # 收件人
        self.driver.find_element_by_xpath(str+'tr[@class="fwReceiver"]/td/ul/li/input').send_keys('1721906562@qq.com')
        time.sleep(1)
        # 主题
        self.driver.find_element_by_xpath(str+'input[@name="subj"]').send_keys('python test')
        time.sleep(2)
        # 切换iframe
        iframe_edit = self.driver.find_elements_by_xpath(str+'div[@id="SinaEditor"]/iframe')
        self.driver.switch_to.frame(iframe_edit[0])
        time.sleep(1)
        # 内容
        self.driver.find_element_by_xpath('/html/body').send_keys('测试')
        time.sleep(2)
        # 回到主文档
        self.driver.switch_to.default_content()

        # 发送
        self.driver.find_element_by_xpath('//*[@id="panel_main"]/div[1]/span/span[1]/a/i[2]').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
