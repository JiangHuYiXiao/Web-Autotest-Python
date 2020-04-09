# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 9:01
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# find_element一类的方法都是用于定位的
# find_elements一类的方法，都是要用于查找的，有返回值，返回一个列表，可以通过索引获取到元素
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
list1 = driver.find_elements_by_tag_name('input')
list1[0].send_keys('金蝶')
sleep(2)
print(list1,len(list1),list1[0])
print(type(list1))
driver.quit()
