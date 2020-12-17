# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/8/13 8:48
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import time,logging
now_time = time.strftime('%Y_%m_%d %H_%M_%S')    # 2020_01_01 12_14_05

class Log():
    def __init__(self):

        # 初始化日志对象
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s%(filename)%s[line:%(lineno)d]%(levelname)s%(message)s',
            datefmt='%Y_%m_%d %H_%M_%S',
            filename='./../report/'+now_time[:10]+'/log/'+now_time[-8:]+'.log',
            filemode='w'
        )

    def addlog(self,page,func,desc):
        outlog = page + ':'+func+':' +desc
        logging.info(outlog)