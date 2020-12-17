# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/31 8:24
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import HTMLTestRunner,time,os

def make_dir(path):
    if not(os.path.exists(path)):
        os.makedirs(path + '/html')
        os.makedirs(path + '/png')
        os.makedirs(path + '/log')

# now_time = time.strftime('%Y_%m_%d_%H_%M_%S')