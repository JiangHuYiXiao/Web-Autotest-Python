# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/1/22 14:25
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
CSS定位：比xpath定位更快，是通过css样式来定位的，相比于xpath的全局扫描定位更快。
#表示id
.表示class
>表示所有的儿子
 空表示所有的儿子，孙子等
 伪类选择器：
 first-child表示第一个子元素，后面不能加括号
 nth-child（2）表示第二个子元素
 last-child表示最后一个子元素，后面不能加括号

xpath定位：
find_element_by_xpath('//input[@id="kw"]')       id
find_element_by_xpath('//input[@name="wd"]')        其他属性
find_element_by_xpath('//*[@id="header-link-wrapper"]/li[5]/a')  序号
/ 表示子元素
// 表示所有的父子元素

parent选择当前节点的上一层父节点
    # //img[@alt='div1']/parent::div                  div1的上一层div

child选择当前节点下层的所有子节点
    # //img[@alt='div1']/child::div                  div1的下层的所有div

ancestor选择当前节点的所有上层节点
    # //img[@alt='div1']/ancestor::div                  div1的上一层div
'''
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Focus():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 隐示等待
        self.driver.implicitly_wait(3)
        self.driver.get('http://www.baidu.com/')

    def test_css(self):
        # self.driver.find_element_by_css_selector('input#kw').send_keys('米奇')
        res = self.driver.find_elements_by_css_selector('div#head div')
        print(res)
        # self.driver.find_element(by=By.CSS_SELECTOR,value='input[id="kw"]').send_keys('上梁不正下梁歪')
        # 直接等待
        time.sleep(3)
    def test_xpath(self):
        self.driver.find_element_by_xpath('//input[@id="kw"]')
        self.driver.find_element_by_xpath('//input[@name="wd"]')



    def teardown_class(self):
        self.driver.quit()


# 我们可以直接在浏览器的console命令窗口输入命令测试我们的定位方法是否可以
# xpath定位方法：
# $x('//input[@id="kw"]')

# css定位方法：
# $('#kw')
