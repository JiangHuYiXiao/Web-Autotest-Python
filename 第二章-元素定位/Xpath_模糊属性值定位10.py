# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 8:08
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# Xpath多个class之间不加任何符合，CSS定位需要加.
# 模糊属性值定位是通过starts_with函数和contains函数来进行定位的
# starts_with              以什么开头
# contains                 包含什么
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//input[contains(@class,"word")]').send_keys('霸王别姬')
driver.find_element_by_xpath('//a[starts-with(@value,百)]').click()
sleep(2)
driver.quit()