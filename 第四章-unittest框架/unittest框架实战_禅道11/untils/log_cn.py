# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/21 8:09
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
创建目录的方法，按照每天生成报告
'''

import unittest,time,os
nowtime = time.strftime('%Y_%m_%d_%H_%M_%S')

def make_report(path):
    if not(os.path.exists(path)):
        os.makedirs(path+'/html')
        os.makedirs(path+'/png')

