# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/12 8:23
# @Software       : Python_study
# @Python_verison : 3.7
import unittest

class Case01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # '测试类开始方法，在一个类中只执行一次'
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        # '测试类结束方法，在一个类中只执行一次'
        print('tearDownClass')

    def setUp(self):
        # 用例执行开始的方法，在每一个用例执行前面都会执行一次
        print('setUp')

    def tearDown(self):
        # 用例执行结束的方法，在每一个用例执行后面都会执行一次
        print('tearDown')

    def test_case10(self):
        print('test_case10')
    # @unittest.skip

    def test_case11(self):
        print('test_case11')


class Case02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # '测试类开始方法，在一个类中只执行一次'
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        # '测试类结束方法，在一个类中只执行一次'
        print('tearDownClass')

    def setUp(self):
        # 用例执行开始的方法，在每一个用例执行前面都会执行一次
        print('setUp')

    def tearDown(self):
        # 用例执行结束的方法，在每一个用例执行后面都会执行一次
        print('tearDown')

    def test_case20(self):
        print('test_case20')

    # @unittest.skip
    def test_case21(self):
        print('test_case21')

# 运行方法1：
# 执行当前文件中的所有test开头的用例使用unittest.main()
# if __name__ == '__main__':
#     unittest.main()

# 运行方法2：
# 执行几条测试用例

# suite = unittest.TestSuite()
# suite.addTest(Case01('test_case10'))     # 不能连着写suite = unittest.TestSuite().addTest(Test_Case01('test_case10'))
# suite.addTest(Case02('test_case20'))
# if __name__ =='__main__':
#     unittest.TextTestRunner().run(suite)


# 运行方法3：
# 执行某些测试类
suite1 = unittest.TestLoader().loadTestsFromTestCase(Case01)
suite2 = unittest.TestLoader().loadTestsFromTestCase(Case02)
# suite = unittest.TestSuite([suite1,suite2])
suite = unittest.TestSuite([suite1])
unittest.TextTestRunner().run(suite)
#

# 运行方法4：
dir = './'
suite = unittest.defaultTestLoader.discover(dir,pattern='test*.py')
unittest.TextTestRunner().run(suite)