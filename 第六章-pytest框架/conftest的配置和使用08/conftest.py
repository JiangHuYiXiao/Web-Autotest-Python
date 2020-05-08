# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/8 8:00
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7


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