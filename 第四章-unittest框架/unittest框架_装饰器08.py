# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 8:49
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 在运行测试时，有时需要直接跳过某些测试用例，或者当前用例符合某个条件时跳过测试，又或者直接将测试用例设置为失败
# unittest提供了实现这些需求的装饰器

# 装饰器：
# unittest.skip(reason='')                              # 无条件的跳过装饰的测试用例，说明跳过的原因，跳过则输出reason

# unittest.skipIf(condition='',reason='')               # 如果条件为真，，跳过则输出reason

# unittest.skipUnless(condition='',reason='')           # 当条件为真时执行测试用例，否则跳过被装饰的用例，跳过则输出reason

# unittest.expectedFailure()                            # 测试标记为失败，不管执行结果是否为失败，统一标记为失败

# classmethod   类方法，装饰类，表示该类中这个方法执行一次

# 1、装饰方法
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        print('test case start')
    @unittest.skip('无条件的跳过test_skip用例')
    def test_skip(self):
        print('test_skip')

    @unittest.skipIf(3 > 2,'当条件为真时跳过测试用例')
    def test_skipIf(self):
        print('test_skipIf')
    @unittest.skipIf(3 > 4,'当条件为真时跳过测试用例')
    def test_skipIf2(self):
        print('test_skipIf2')

    @unittest.skipUnless(3 > 2,'当条件为真时执行测试用例')
    def test_skipUnless(self):
        print('test_skipUnless')

    @unittest.expectedFailure
    def test_exceptFailure(self):
        print('test_expectFailure')
    def tearDown(self):
        print('test case end')

if __name__ == '__main__':
    unittest.main()


# 2、装饰类，也可以直接装饰测试类
# import unittest
#
# @unittest.skip('无条件的跳过test_skip用例')
# class Test(unittest.TestCase):
#     def setUp(self):
#         print('test case start')
#
#     def test_skip(self):
#         print('test_skip')
#
#     def test_skipIf(self):
#         print('test_skipIf')
#
#     def test_skipIf2(self):
#         print('test_skipIf2')
#
#     def test_skipUnless(self):
#         print('test_skipUnless')
#     def tearDown(self):
#         print('test case end')
#
# if __name__ == '__main__':
#     unittest.main()