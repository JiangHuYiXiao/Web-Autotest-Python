# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/7 9:20
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
参数解析
fixture(scope="function", params=None, autouse=False,ids=None, name=None):
scope 有四个级别参数：function, class、Module、session
params: 一个可选的参数列表，它将导致多个参数调用fixture 功能和所有测试使用它。

autouse: 如果为 True，则为所有测试激活 fixture func 可以看到它。 如果为 False（默认值）则显式需要参考来激活 fixture
ids:每个字符串 id 的列表，每个字符串对应于 params 这样他们就是测试 ID 的一部分。 如果没有提供 ID 它们将从 params 自动生成。
name: fixture 的名称,这默认为装饰函数的名称

'''
import pytest
# 不带参数时默认 scope="function"
@pytest.fixture()               # function，运行两次
def login():
    print("输入账号，密码先登录")
def test_s1(login):
    print("用例 1：需要登录操作")
def test_s2(login):         # 调用login，然后执行login（）
    print("用例 2：登录之后其它动作")




import pytest
@pytest.fixture(scope="module")                 # 只运行一次
def open():
    print("打开浏览器，并且打开百度首页")

def test_s3(open):
    print("用例 1：搜索 python-1")

def test_s4(open):
    print("用例 2：搜索 python-2")

if __name__ == "__main__":
    pytest.main()

