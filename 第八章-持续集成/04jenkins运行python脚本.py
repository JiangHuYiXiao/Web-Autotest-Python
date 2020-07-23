# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/22 8:05
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、jenkins运行python脚本方式1：通过windows批处理命令运行指定的python运行文件
# 首先需要设置python环境变量，在jenkins的系统设置中配置环境变量：Path：C:\Users\Administrator\AppData\Local\Programs\Python\Python37，如果调用不了chrome浏览器也需要把浏览器程序加在path中
    # windows批处理命令为：cmd.exe python F:\Web-Autotest-Python\第八章-持续集成\run.py
# 或者
    # python F:\Web-Autotest-Python\第八章-持续集成\run.py

# 2、在jenkins中安装python插件
