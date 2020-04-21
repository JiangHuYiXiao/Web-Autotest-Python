# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/21 19:56
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
截图方法
'''
import time
now = time.strftime('%Y_%m_%d')
now1 = time.strftime('%H_%M_%S')
def screenshot(driver,filename):
    driver.get_screenshot_as_file('F:/Web-Autotest-Python/第四章-unittest框架/nittest框架实战_禅道11/report/'+now+'/png/'+now1+filename+'.png')