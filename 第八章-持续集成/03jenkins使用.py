# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/21 20:14
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、使用jiangtao_jiang登录jenkins
# 2、创建jenkins工程，维护general增加工程描述
# 3、源码管理一般都是有三个（无，svn，git）如果git和svn的插件都安装完成则有三个
# 4、构建触发器，一般常用定时构建Build periodically，格式为（* * * * *）H/30 * * * *表示每隔30分钟执行一次
# 5、构建环境选择
# 6、构建步骤，也就是执行脚本，如果在windows上执行批处理命令，应该选择Execute Windows batch command
# 7、增加构建后操作
# 8、保存，应用后可以选择立即构建或者等自动定时构建