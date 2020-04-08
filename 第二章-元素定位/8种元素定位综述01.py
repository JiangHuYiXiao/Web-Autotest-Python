# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/8 10:41
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
driver=webdriver.Chrome()

# 1、id定位
driver.find_element_by_id('')
# 2、class_name定位
driver.find_element_by_class_name('')
# 3、tag_name定位
driver.find_element_by_tag_name('')

# 4、link_text文本定位
driver.find_element_by_link_text('')

# 5、这个partial link定位是对link的一种补充，用于一些较长的文本链接，这时候我们可以取文本的一部分来进行定位
driver.find_element_by_partial_link_text('')

# 6、name属性定位
driver.find_element_by_name('')

# 7、css_selector选择器定位
driver.find_element_by_css_selector('')

# 8、xpath定位
driver.find_element_by_xpath('')