# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 8:28
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# Xpath轴（Axes）定位：
# 1、parent选择当前节点的上一层父节点
    # //img[@alt='div1']/parent::div                  div1的上一层div

# 2、child选择当前节点下层的所有子节点
    # //img[@alt='div1']/child::div                  div1的下层的所有div

# 3、ancestor选择当前节点的所有上层节点
    # //img[@alt='div1']/ancestor::div                  div1的上一层div

# 4、通过text()函数定位
    # //a[text()="百度一下"]
    # //a[.="百度一下"]
