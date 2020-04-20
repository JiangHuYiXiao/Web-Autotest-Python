# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/17 8:24
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest,HTMLTestRunner,time
from untils.email_tools import SendMailAttach
dir = './case'
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='test*.py')


if __name__ =='__main__':
    now = time.strftime('%Y_%m_%d %H_%M_%S')
    filename = ('./report/html/'+now+'.html')
    file = open(filename,mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='禅道测试报告',description='测试创建编辑用例和创建编辑bug')
    runner.run(suite)
    time.sleep(3)
    SendMailAttach(filename)