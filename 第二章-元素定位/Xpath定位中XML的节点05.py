# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 9:01
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# Xpath是XML_path语言的缩写，是一门在XML文档中查找信息的语言。
# 它在XML稳文档中通过元素和属性进行导航，主要用于在XML中选择节点。
# Xpath语言可以用于整个文档中沿着paht或step来寻找指定的节点。说白了就是通过路径来定位元素，一个元素就是一个节点。
# 比CSS定位灵活，但是速度稍逊。
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
# driver.find_element_by_xpath('//*[@id="ww"]').send_keys('金蝶')    # 通过属性定位，查找,鼠标右键可以获取到浏览器给出的Xpath
driver.find_element_by_xpath('html/body/div/div/table/tbody/tr/td/table/tbody/tr/td/div/span/input').send_keys('金蝶')        # 通过绝对路径查找
sleep(2)
driver.quit()