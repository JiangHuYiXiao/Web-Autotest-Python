# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/9 9:14
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest,HTMLTestRunner
suite = unittest.defaultTestLoader.discover(start_dir='./',pattern='test_ddt.py')

if __name__ =='__main__':
    file = open('./report.html',mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='ddt测试',description='ddt')
    runner.run(suite)
