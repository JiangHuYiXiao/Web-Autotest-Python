# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/13 9:32
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、js的弹出窗口有三种，alert(),onfirm(),prompt()
# 2、这三种弹框首先我们都必须把driver到这个窗口上，driver.switch_to.alert()
# 示例1：alert弹窗
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.implicitly_wait(6)
# driver.maximize_window()
# driver.get('http://localhost:63342/Web-Autotest-Python/第三章-常用WebAPI操作/alert弹窗.html')
#
# # sleep(2)
# driver.find_element_by_xpath('//input[@value="单击此按钮弹出窗口"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()                # 确定
# sleep(2)
# driver.quit()

# 示例2：confirm弹窗
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.implicitly_wait(6)
# driver.maximize_window()
# driver.get('http://localhost:63342/Web-Autotest-Python/第三章-常用WebAPI操作/alert弹窗.html')
#
# # sleep(2)
# driver.find_element_by_xpath('//input[@value="单击此按钮弹出窗口"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# # alert.accept()                      # 确定
# alert.dismiss()                     # 取消
# sleep(2)
# driver.quit()

# 示例3：prompt
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()
driver.get('http://localhost:63342/Web-Autotest-Python/第三章-常用WebAPI操作/alert弹窗.html')

# sleep(2)
driver.find_element_by_xpath('//input[@value="单击此按钮弹出窗口"]').click()
sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys('江湖一笑')             # chrome输入无效，firefox可行
sleep(2)
alert.accept()                      # 确定
# alert.dismiss()                     # 取消
sleep(2)
driver.quit()