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

def test_01(open1):
    print('用例1,搜索一休')

def test_11(open1):
    print('用例11,搜索一休')

def test_02(open2):
    print('用例2，搜索江湖')

def test_12(open2):
    print('用例2，搜索江湖')

class Test_baidu():
    def test_03(self,open3):
        print('用例3，搜索寒山孤影')
    def test_04(self,open3):
        print('用例3，搜索江湖故人')

if __name__ =='__main__':
    pytest.main()