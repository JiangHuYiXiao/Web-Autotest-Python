# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/27 9:01
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest
dir = './../case/'
print(dir)
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='baidu_*.py')
runer = unittest.TextTestRunner()
runer.run(suite)