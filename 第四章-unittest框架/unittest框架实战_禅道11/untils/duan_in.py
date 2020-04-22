# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/21 9:16
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
断言优化
'''
import unittest,time
from selenium.common.exceptions import NoSuchElementException
from untils.screen_shot import screenshot
from untils.log_cn import write_log
def duan_in(driver,yu,shi,filename):
    try:
        unittest.TestCase().assertIn(yu,shi,filename)
    except NoSuchElementException as e:
        # screenshot(driver, filename)
        # write_log('预期%r : 实际%r' % (yu, shi))
        print('元素未找到')
        unittest.TestCase().assertIn(yu, shi, filename)
    except AssertionError as e:
        screenshot(driver,filename)
        write_log('预期%r : 实际%r'%(yu,shi))
        print('预期结果和实际结果不相等')
        unittest.TestCase().assertIn(yu, shi, filename)
    except Exception as e:
        print('未知错误')
        unittest.TestCase().assertIn(yu,shi,filename)
    else:
        print('执行通过')

def duan_equal(yu,shi,case):
    try:
        unittest.TestCase().assertEqual(yu,shi,case)
    except NoSuchElementException as e:
        print('元素未找到')
    except AssertionError as e:
        print('预期结果和实际结果不相等')
    except Exception as e:
        print('未知错误')
    else:
        print('执行通过')

# 还可以添加其他断言的方法