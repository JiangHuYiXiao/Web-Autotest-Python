# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/27 9:01
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest,HTMLTestRunner,time,HTMLTestRunner_PY3
from baidu_tools.html_report import make_dir
from baidu_tools.send_email import SendMailAttach
from baidu_tools.screen_shot import screen_shot
now_time = time.strftime('%Y_%m_%d %H_%M_%S')    # 2020_01_01 12_14_05
dir = './../case/'
print(dir)
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='baidu_news.py')
report_file = make_dir('./../report/'+now_time[:10])

html_file = ('./../report/'+now_time[:10]+'/html/'+now_time[-8:]+'.html')
# png_file = ('./../report/'+now_time[:10]+'/png/')
# log_file = ('./../report/'+now_time[:10]+'/log/')
with open(file=html_file,mode='wb') as htmlfile:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=htmlfile,title='百度新闻测试',description='百度新闻搜索测试报告')
    runner.run(suite)
    SendMailAttach(html_file)



