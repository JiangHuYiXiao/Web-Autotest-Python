# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/9 18:47
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.jd.com/')
# 1、相对路径写法1：通过标签中的属性id来定位
# // 代表相对路径
# * 代表所有的标签对
# 标签对后面接中括号
# @ 后面接的是属性
# = 后面是属性值
# / 后面就是路径
driver.find_element_by_xpath('//*[@id="areamini"]/span').click()
sleep(2)
# 2、相对路径写法2：通过标签的上面或者后面标签来定位 ../ 上一个 ./当前
# //*[@id="ttbar-mycity"]/div/div[2]/div/div/div[8]/a

# driver.find_element_by_xpath('//a[@id="areamini"]/../div/div[2]/div/div/div[7]/a').click()

driver.find_element_by_xpath('//a[@id="areamini"]/../div/div[2]/div/div/div//a[@data-id="7"]').click()
sleep(2)
driver.quit()