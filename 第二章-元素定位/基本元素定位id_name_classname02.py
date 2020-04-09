# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 8:07
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 1、id定位:一个HTML页面的id一般来说唯一，谨慎点可以在页面查找下。

test_id = driver.find_element_by_id('kw')
test_id.send_keys('金蝶')
# 或者直接写成
# driver.find_element_by_id('kw').send_keys('金蝶')
sleep(2)
driver.quit()

# 2、name属性定位：有的标签是没有name属性的
driver.find_element_by_name('wd').send_keys('金蝶')
sleep(2)
driver.quit()


# 3、class_name定位，通过标签的class属性定位：
# 因为标签的class属性的类大多数不是唯一一个，一般都是一个class有多个类，或者多个标签有这个class类，所以这个定位比较少用
driver.find_element_by_class_name('s_ipt').send_keys('金蝶')
sleep(2)
driver.quit()
'''

# 示例：百度新闻标题，应用上面三种方法
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()                # 控制浏览器，放最大
driver.get('http://news.baidu.com/')
driver.find_element_by_name('word').send_keys('辽宁号航空母舰')
sleep(2)
driver.find_element_by_id('s_btn_wr').click()
sleep(2)
driver.get('http://news.baidu.com/')
driver.find_element_by_class_name('help').click()
sleep(2)
driver.quit()