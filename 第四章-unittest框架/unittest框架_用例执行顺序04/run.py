# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 15:59
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from TestCase1 import MyTestCase1
from TestCase2 import MyTestCase2
import unittest

# 这种有套件的执行顺序就是根据add的顺序
suite = unittest.TestSuite()
suite.addTest(MyTestCase1('test_baidu1'))
suite.addTest(MyTestCase2('test_baidu2'))
suite.addTest(MyTestCase1('test_sogou1'))
suite.addTest(MyTestCase2('test_sogou2'))

if __name__ =='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
