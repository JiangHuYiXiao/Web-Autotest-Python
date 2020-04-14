# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 19:59
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest
dir = './case/'
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='Tes*.py')
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
