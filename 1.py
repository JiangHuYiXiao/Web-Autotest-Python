# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/12/1 8:55
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import pytest
@pytest.fixture(scope="module")                 # 只运行一次
def open():
    print("打开浏览器，并且打开百度首页")

def test_s3(open):
    print("用例 1：搜索 python-1")

def test_s4(open):
    print("用例 2：搜索 python-2")
