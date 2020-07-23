# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/22 8:37
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7



import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com/')
time.sleep(3)
driver.find_element_by_xpath('//input[@id="kw"]').send_keys('胡锡进')
time.sleep(2)
driver.find_element_by_xpath('//input[@id="su"]').click()
time.sleep(2)
now = time.strftime('%Y_%m_%d %H_%M_%S')
with open('F:/Web-Autotest-Python/第八章-持续集成/05jenkins运行python+selenium自动化脚本/'+now+'.txt',mode='w',encoding='utf-8')as file:
    file.write(driver.page_source)
driver.quit()