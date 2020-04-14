# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 8:56
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest
from unittest框架_TestCase import MyTestCase
suite = unittest.TestSuite()
suite.addTest(MyTestCase('test_baidu'))
suite.addTest(MyTestCase('test_sogou'))

if __name__ == '__main__':
    # 执行方式1：
    # print(__name__)
    # unittest.main()
    # 执行方式2：
    runner = unittest.TextTestRunner()
    runner.run(suite)