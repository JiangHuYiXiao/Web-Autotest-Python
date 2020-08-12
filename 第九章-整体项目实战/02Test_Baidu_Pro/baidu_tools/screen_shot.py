# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/8/11 8:29
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

import time
import selenium
Ymd = time.strftime('%Y_%m_%d')
HMS = time.strftime('%H_%M_%S')
def screen_shot(driver,filename):
    driver.get_screenshot_as_file('./../report/' + Ymd + '/png/' + HMS + filename+'.png')




