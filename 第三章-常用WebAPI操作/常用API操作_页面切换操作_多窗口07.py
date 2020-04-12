# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/12 14:56
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、driver.switch_to.window()           切换窗口
# 一般用于前后台交互，或者数据对比、流程验证
# 需要使用变量存储所有句柄，然后通过索引访问指定页面

# 2、更新窗口,在原窗口基础上
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'t')


# 3、新建一个窗口，原窗口不关闭
# driver.excute_script("window.open('http://www.sogou.com')")

# 示例1：
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://www.baidu.com')
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys('盗墓笔记')
# driver.find_element_by_xpath('//input[@id="su"]').click()
# sleep(2)
# print(driver.window_handles)
# print(driver.current_window_handle)
# # 打开新窗口，新网页,在同一个窗口中
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'t')
# driver.get('http://www.sogou.com')
# driver.find_element_by_xpath('//input[@class="sec-input active"]').send_keys('鬼吹灯')
# driver.find_element_by_xpath('//input[@id="stb"]').click()
# print(driver.window_handles)
# print(driver.current_window_handle)
# sleep(2)
# driver.quit()

# 示例2：
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.find_element_by_xpath('//input[@id="kw"]').send_keys('盗墓笔记')
driver.find_element_by_xpath('//input[@id="su"]').click()
sleep(2)
print(driver.window_handles)
print(driver.current_window_handle)

# 打开新窗口，新网页,在不同窗口中
driver.execute_script('window.open("http://www.sogou.com")')
hands = driver.window_handles
print(driver.window_handles)
print(driver.current_window_handle)
driver.switch_to.window(hands[1])
driver.find_element_by_xpath('//input[@class="sec-input active"]').send_keys('鬼吹灯')
driver.find_element_by_xpath('//input[@id="stb"]').click()
print(driver.window_handles)
print(driver.current_window_handle)
sleep(2)
driver.quit()