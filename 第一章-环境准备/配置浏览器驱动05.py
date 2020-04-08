# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/8 9:14
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、浏览器驱动下载
# 1.1、下载webdriver
#     chromedriver.exe的驱动器：
#     地址：http://chromedriver.storage.googleapis.com/index.html，选择对应的各个版本，尽量保证驱动和浏览器是一个版本，或者驱动比浏览器高一点点。
# 1.2、Firefox的驱动器
#     地址：https://github.com/mozilla/geckodriver/releases/
# 1.3、IE浏览器驱动
#     地址：http://selenium-release.storage.googleapis.com/index.html

# 2、浏览器驱动配置
#     需要将下载的各个浏览器驱动放到刚上面python配置的环境变量的目录下中的一个
#     C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Scripts\;
#     C:\Users\Administrator\AppData\Local\Programs\Python\Python37\
# 3、驱动试用

from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(2)
driver.quit()

# 返回Process finished with exit code 0说明配置成功