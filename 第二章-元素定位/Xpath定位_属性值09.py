# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 20:24
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com/')   # //*[@id="sbox"]/tbody/tr/td[1]/div[1]/a/img
driver.find_element_by_xpath('//img[@alt="百度新闻"]').click()
sleep(2)
driver.quit()
