# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/11 9:53
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# is_displayed                  是否可见
# is_enabled                    是否可操作
# is_slected                    是否选中
# 这些属性可以作为我们后续断言的方法，判断用例是否执行通过

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://news.baidu.com')
# longinEle = driver.find_element_by_link_text('登录')
# print(longinEle.is_displayed())
# print(longinEle.is_enabled())
# print(longinEle.is_selected())
# sleep(2)
# driver.quit()



from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://news.baidu.com')
sleep(2)
print(driver.window_handles)
longinEle = driver.find_element_by_link_text('登录')
longinEle.click()
# 判断登录按钮是否可见，可操作
print(longinEle.is_displayed())
print(longinEle.is_enabled())

print(driver.current_window_handle)
# driver.switch_to.window()
# 点击登陆后，判断下次自动登录checkbox是否勾选
# remberEle = driver.find_element_by_name('memberPass')
remberEle = driver.find_element_by_css_selector('input[class="pass-checkbox-input.pass-checkbox-memberPass"]')
print(remberEle.is_selected())
sleep(2)
remberEle.click()
print(remberEle.is_selected())

driver.quit()


