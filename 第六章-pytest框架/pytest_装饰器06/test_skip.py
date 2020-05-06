# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/2 9:19
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
1、pytest.mark.skip：
        可以标记无法在某些平台上运行的测试功能，或者希望失败的测试功能。
2、skip if ：
        意味着在不满足某些条件时才希望测试通过，否则 pytest应该跳过运行测试。
        常见示例是在非 Windows 平台上跳过仅限Windows 的测试，或跳过测试依赖于当前不可用的外部资源。
3、xfail ：
        类似于失败，但是用例会执行，这个可以应用于某些用例之间有关联，前后条件的情况
        意味着你希望测试由于某种原因而失败。 一个常见的例子是对功能的测试尚未实施，或尚未修复的错误。。

'''
from time import sleep
from selenium import webdriver
import pytest
driver = webdriver.Chrome()

@pytest.mark.skip               # 标记该用例直接跳过
def test_skip1():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title == '百度一下，你就知道')

@pytest.mark.skip(reason='本轮跳过')                # 标记用例本轮跳过，给出一个原因
def test_skip2():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title == '百度一下，你就知道')

def skip4():
    return True

def skip5():
    return False
def test_skip3():
    driver.get('https://www.sohu.com/')
    sleep(2)
    if not skip4():     # 调用函数skip4，返回一个True，not True，不会执行跳过，
        pytest.skip('本用例跳过')
    assert(driver.title=='搜狐')
    driver.quit()

def test_skip4():
    driver.get('https://www.sohu.com/')
    sleep(2)
    if not skip5():     # 调用函数skip5，返回一个False，not False，执行跳过，
        pytest.skip('本用例跳过4')
    assert(driver.title=='搜狐')
    driver.quit()
