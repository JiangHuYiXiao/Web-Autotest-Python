# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/1 8:24
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
def add(a,b):
    return(a + b)

def test_add1():
    assert(add(2,3)) == 5

def test_add2():
    assert(add(5,3)) == 8

def test_add3():
    assert(add(5,3)) == 7