# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 19:45
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# *********注意点，很多网页登录的html和不登录的html网页元素和布局是不一致的。**********
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
# driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[5]/a').click()
sleep(2)
# driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[last()-4]/a').click()   # 倒数第四个
sleep(2)
driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[position()<4]/a').click()   # 顺序数小于4，一般取第1个
sleep(2)
# driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[position()>4]/a').click()   # 顺序数大于4，一般取第5个
sleep(2)
driver.quit()