# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 12:26
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、页面自带属性操作
    # title     网页标题
    # name      浏览器名称
    # session_id            动态id值
    # maximize_window       窗口最大化   因为selenium只对当前页面可见的元素进行操作
    # driver.set_window_size(400,800)  设置窗体大小
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//input[@class="word"]').send_keys('selenium')
driver.find_element_by_xpath('//input[@id="s_btn_wr"]').click()
sleep(2)
print(driver.title)             # 返回网页的标题：百度资讯搜索_selenium
print(driver.name)              # 返回浏览器的名称：chrome，可以应用后面进行兼容性测试
print(driver.session_id)         # e404fcff6d75f6b82bf0fd7933ac1d15

driver.quit()
