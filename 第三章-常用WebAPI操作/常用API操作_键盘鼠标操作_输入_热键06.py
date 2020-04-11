# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/11 21:34
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、send_keys()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_xpath('').send_keys('')
driver.quit()

