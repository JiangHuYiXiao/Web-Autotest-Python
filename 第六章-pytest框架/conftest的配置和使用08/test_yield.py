# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/8 8:36
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
使用yield不会结束函数，而是会等到调用的函数执行结束后，再执行yield后面的语句
'''
import pytest
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行 teardown!")
    print("最后关闭浏览器")
def test_s1(open):
    print("用例 1：搜索 python-1")
def test_s2(open):
    print("用例 2：搜索 python-2")

@pytest.fixture(scope="function")
def open1():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行 teardown!")
    print("最后关闭浏览器")

def test_s3(open1):
    print("用例 3：搜索 python-3")

def test_s4(open1):
    print("用例 4：搜索 python-4")

if __name__ == "__main__":
    pytest.main()
