# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 8:42
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
# 1、link_text定位：这种一般用于a标签，也应用于其他标签的文字
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://news.baidu.com')
# driver.find_element_by_link_text('习近平主持中共中央政治局常务委员会会议').click()
# sleep(2)
# driver.quit()

# 2、partial_lind_text定位，这个一般标签的文字较长时，我们可以使用这个来通过一部分文字定位
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://news.baidu.com')
# driver.find_element_by_partial_link_text('政治局常务委员会会议').click()
# sleep(2)
# driver.quit()

# 3、tag_name:通过标签来定位元素，很少用，因为一个htm的标签都是那些div、input、a、p、h，这个一般结合我们后面的elements方法一起使用
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_tag_name('input')
driver.quit()

