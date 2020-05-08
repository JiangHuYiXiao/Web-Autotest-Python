# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/8 8:47
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
使用pytest.mark.parametrize装饰器可以实现测试用例的参数化。
pytest.mark.parametrize('参数'，[value])
'''
import pytest

# 一个参数
list1 = ['寒山孤影','江湖故人','相逢何必曾相识']
@pytest.mark.parametrize('par1',list1)
def test_01(par1):
    print('用例_',par1)

# 两个参数
list2 = [('寒山孤影',1),('江湖故人',2),('相逢何必曾相识',3)]
@pytest.mark.parametrize('par1,par2',list2)
def test_01(par1,par2):
    print(par2,'用例_',par1)

# 通过参数化标记单个测试实例，为失败
@pytest.mark.parametrize("test_input,expected",
   [("3+5", 8),("2+4", 6),
     pytest.param("6 * 9", 42,
    marks=pytest.mark.xfail)
    ,])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ =='__main__':
    pytest.main()
