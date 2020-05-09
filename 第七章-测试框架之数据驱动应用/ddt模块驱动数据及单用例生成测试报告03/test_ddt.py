# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/9 8:28
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# import unittest
# class Test_ddt(unittest.TestCase):
#     '''unittest框架测试'''
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#     def test_add(self,arg1,arg2,arg3,except_data):
#         sum = 0
#         sum = arg1+arg2+arg3
#         self.assertEqual(sum,except_data)

# 像上面这个情况我们无法把参数传递到test_add方法中，这个时候我们就需要使用到数据驱动
import ddt
import unittest

@ddt.ddt            # 声明ddt
class Test_ddt(unittest.TestCase):
    '''unittest框架测试+ddt框架实现数据驱动'''
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data([1,2,3,6],[2,4,6,12],[1,2,4,5])               # 添加测试数据,多个数据之间用逗号分开，有多少形参传多少数据，位置参数对应
    @ddt.unpack             # 表示将测试数据传递给形参
    def test_add(self,arg1,arg2,arg3,except_data):
        sum = 0
        sum = arg1+arg2+arg3
        self.assertEqual(sum,except_data)

# 这样的运行是有三条测试用例，在报告和统计中，且用例的名称为test_add+参数+断言
if __name__ =='__main__':
    unittest.main()
