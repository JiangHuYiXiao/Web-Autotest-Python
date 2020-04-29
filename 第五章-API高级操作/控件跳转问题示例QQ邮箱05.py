# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/28 17:23
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
有的时候在页面进行定位时候，默认会进入一个iframe，这个时候，
如果要操作iframe外的元素先要先切换到主文档，然后要操作iframe中的元素需要再次切换到iframe
'''
import unittest,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Test_QQEmail(unittest.TestCase):
    '''qq邮箱操作类'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()
        self.driver.get('https://mail.qq.com/')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        print('用例执行start')

    def tearDown(self):
        print('用例执行end')

    def test_01login_email(self):
        '''登录qq邮箱用例'''
        yx = self.driver.find_elements_by_xpath('//iframe[@id="login_frame"]')
        self.driver.switch_to.frame(yx[0])
        self.driver.find_element_by_xpath('//span[@id="img_out_1721906562"]').click()
        time.sleep(4)
        # hands = self.driver.window_handles
        # print(self.driver.current_window_handle,hands)
        # # self.driver.switch_to.window(hands[])
        try:
            self.assertEqual('QQ邮箱',self.driver.title,'登录失败')
        except AssertionError as e:
            self.assertEqual('QQ邮箱', self.driver.title, '登录失败')
        except NoSuchElementException as e:
            print('预期结果和实际结果不相等')
            self.assertEqual('QQ邮箱',self.driver.title,'登录失败')
        except Exception as e:
            print('未知错误')
        else:
            print('执行通过')


    def test_02write_email(self):
        '''编写发送邮件用例'''
        # print(self.driver.page_source)
        # 点击写信
        self.driver.find_element_by_xpath('//a[@id="composebtn"]').click()
        time.sleep(2)
        # 切换到第一层iframe（mainFrame）
        xx = self.driver.find_elements_by_xpath('//iframe[@id="mainFrame"]')
        self.driver.switch_to.frame(xx[0])
        self.driver.find_element_by_xpath('//div[@id="toAreaCtrl"]/div[2]/input').send_keys('19170920820@163.com')
        time.sleep(2)
        # 跑腳本沒有抄送這個
        # ee = self.driver.find_elements_by_xpath('//div[@id="ccAreaCtrl"]/div[2]//following::b[@unselectable="on"]')#.send_keys('1163270704@qq.com')
        # print(len(ee))
        # time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="subject"]').send_keys('qq邮箱测试')
        time.sleep(2)
        # 切换到第二层iframe，往mainframe再切入进里面的iframe
        qq = self.driver.find_elements_by_xpath('//div[@id="QMEditorArea"]/table/tbody/tr[2]/td/iframe')
        print(len(qq))
        self.driver.switch_to.frame(qq[0])
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body').send_keys('寒江孤影，江湖故人，相逢何必曾相识!')
        time.sleep(2)
        # 切回到主文档
        self.driver.switch_to.default_content()
        # 在切到mainiframe
        self.driver.switch_to.frame(xx[0])
        # 发送
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
        time.sleep(3)

        self.assertEqual('QQ邮箱 - 写信',self.driver.title,'用例执行失败')

if __name__=='__main__':
    unittest.main()