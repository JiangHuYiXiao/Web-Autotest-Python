# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 17:04
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
# 利用Xpath的绝对路径来定位元素
driver.find_element_by_xpath('html/body/div/div/table/tbody/tr/td/table/tbody/tr/td/div/span/input').send_keys('武汉')
driver.find_element_by_xpath('html/body/div/div/table/tbody/tr/td/table/tbody/tr/td/div/span[2]/input').click()       # 结合索引定位
sleep(2)
driver.quit()
