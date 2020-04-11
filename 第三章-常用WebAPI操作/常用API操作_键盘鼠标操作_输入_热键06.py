# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/11 21:34
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、send_keys(内容或者键盘输入)
# 2、ctrl+A,ctrl+C,ctrl+V，ctrl+X等等热键组合

# 示例1：关1键的输入
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 输入框输入内容
driver.find_element_by_xpath('//input[@id="kw"]').send_keys('鬼吹灯')
sleep(2)
# 输入框全选操作ctrl+A
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'a')
sleep(2)
# 输入框剪切操作ctrl+X
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'x')
sleep(2)
# 输入框全选操作ctrl+V
driver.find_element_by_xpath('//input[@id="kw"]').send_keys(Keys.CONTROL,'v')
sleep(2)
driver.find_element_by_xpath('//input[@id="su"]').click()
sleep(2)
driver.quit()

