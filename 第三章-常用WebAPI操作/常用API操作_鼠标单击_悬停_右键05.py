# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/11 20:00
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、.click() 有的页面元素即使不能操作，但是也可以单击，且不报任何错误
# 2、move_to_element         :鼠标悬停
# 3、content_click()         :鼠标右键

# 1、鼠标悬停示例
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ActionChains      # 鼠标相关操作模块
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com')
# setEle = driver.find_elements_by_xpath('//a[@name="tj_settingicon"]')
# ActionChains(driver).move_to_element(setEle[1]).perform()           # perform()表示提交
# sleep(2)
# # 悬停选择搜索设置
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/a[1]').click()
# sleep(1)
# driver.quit()


# 2、鼠标右键示例
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys         # 键盘操作模块
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
sleep(1)
baidu_log = driver.find_element_by_xpath('//*[@id="lg"]/map/area')
# ActionChains(driver).context_click(baidu_log).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
ActionChains(driver).context_click(baidu_log).perform()
sleep(2)
driver.quit()
