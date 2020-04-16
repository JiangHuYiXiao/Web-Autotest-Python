# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 9:06
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 三种测试报告：HTMLTestRunner,HTMLTestRunner_cn,HTMLTestRunner_PY3

import unittest,HTMLTestRunner,HTMLTestRunner_cn,HTMLTestRunner_PY3

dir = './case/'
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='Test*.py')
if __name__ == '__main__':
    # file = open('./result.html',mode='wb')
    # HTMLTestRunner
    # runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')

    # HTMLTestRunner_cn
    # file = open('./result1.html',mode='wb')
    # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')
    # HTMLTestRunner_PY3
    file = open('./result.html',mode='wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=file,title='百度搜索测试报告',description='含有三条用例，测试中文、英文、拼音的三个的搜索结果')

    runner.run(suite)