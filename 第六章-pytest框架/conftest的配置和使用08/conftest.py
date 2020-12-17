# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/8 8:00
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
conftest文件用来写一些前置条件
conftest.py配置脚本名称是固定的，不能改名称
conftest.py和运行的用例要在同一个pakage下，并且有__init__.py文件
不需要import导入conftest.py，pytest用例会自动查找
'''

import pytest
@pytest.fixture(scope='module')
def open1():
    print('打开浏览器1，并且打开百度首页')

@pytest.fixture(scope='function')
def open2():
    print('打开浏览器2，并且打开百度首页')


@pytest.fixture(scope='class')
def open3():
    print('打开浏览器3,并且打开百度首页')