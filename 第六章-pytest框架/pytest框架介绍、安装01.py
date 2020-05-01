# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/1 8:16
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 1、介绍
    # pytest框架是python的一个单元测试框架，与python自带的unittest框架类似，但是比起unittest框架的运行效率更高，使用起来更加简单。

# 2、特点
    # 非常容易上手，入门简单，文档丰富
    # 能够支持简单的单元测试和复杂的功能测试
    # 支持参数化parametrize,比unittest的ddt更简单
    # 执行测试过程中可以将某些测试skip跳过，或者对某些预期失败的case标记成失败
    # 强大的fixture自定义功能，这个是框架的核心亮点功能
    # pytest-rerunfailures（失败case重复执行）
    # pytest-html（完美html测试报告生成，失败截图展示）
    # allure2漂亮的html报告展示
    # 方便的和jenkins持续集成工具集成
    # 支持运行由nose, unittest，doctest框架编写的测试case

# 3、安装
# pytest是python2默认自带的，python3的版本pytest框架独立出来了，需用pip安装。
# 安装：pip install pytest

# 查看是否安装成功，pytest -version
