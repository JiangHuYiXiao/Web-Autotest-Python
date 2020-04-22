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
nows = time.strftime('%H_%M_%S')
def screenshot(driver,filename):
    driver.get_screenshot_as_file('./report/'+now+'/png/'+nows+filename+'.png')