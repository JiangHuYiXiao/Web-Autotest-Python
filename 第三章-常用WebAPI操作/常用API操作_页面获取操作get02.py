# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 14:08
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、driver.get('url')          获取地址
# 2、driver.get_screenshot_as_file('./tieba.png')            获取网站的截图

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//a[text()="贴吧"]').click()
sleep(2)
driver.get_screenshot_as_file('./tieba.png')
driver.quit()


# 实际应用1：

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//a[text()="贴吧"]').click()
# sleep(2)
try:
    assert 'laofu' in driver.page_source
except Exception as e:
    driver.get_screenshot_as_file('./tieba1.png')
    print('用例执行不通过')
else:
    print('用例执行通过')
driver.quit()


# 实际应用2：
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//a[text()="贴吧"]').click()
# sleep(2)
if 'laofu' in driver.page_source:
    print('用例执行通过')
else:
    driver.get_screenshot_as_file('./tieba2.png')
    print('用例执行不通过')

driver.quit()