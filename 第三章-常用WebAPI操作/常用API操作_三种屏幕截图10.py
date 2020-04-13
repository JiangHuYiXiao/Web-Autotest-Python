# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/13 20:52
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、driver.get_screenshot_as_file('./baidu.png')  图片必须是png格式
# 2、with open('./baidu1.png',mode='wb')as file:
#     file.write(driver.get_screenshot_as_png())
# 3、

# 示例1：
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
# driver.get('http://www.baidu.com')
# sleep(1)
# driver.get_screenshot_as_file('./baidu.png')
# driver.quit()


# 示例2：
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(6)
# driver.get('http://www.baidu.com')
# sleep(1)
# with open('./baidu1.png',mode='wb')as file:
#     file.write(driver.get_screenshot_as_png())
# driver.quit()

# 3、示例3
from selenium import webdriver
from time import sleep
import base64
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get('http://www.baidu.com')
sleep(1)
with open('./baidu2.png',mode='wb')as file:
    file.write(base64.b64decode(driver.get_screenshot_as_base64().encode('ascii')))
driver.quit()