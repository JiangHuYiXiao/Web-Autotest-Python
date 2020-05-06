# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/6 8:54
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# 示例1：
from time import sleep
from selenium import webdriver
import pytest,sys
driver = webdriver.Chrome()
python_version = pytest.mark.skipif(sys.version_info>(3,6),reason='Requires Python3.6 or Lower')               # 如果python版本大于3.6则跳过
@python_version
def test_skip1():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title == '百度一下，你就知道')

def test_skip3():
    driver.get('https://www.sohu.com/')
    sleep(2)
    assert(driver.title=='搜狐')
    driver.quit()


# 示例2：
from time import sleep
from selenium import webdriver
import pytest
from level import test_level
driver = webdriver.Chrome()

@test_level
def test_skip1():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title == '百度一下，你就知道')

def test_skip3():
    driver.get('https://www.sohu.com/')
    sleep(2)
    assert(driver.title=='搜狐')
    driver.quit()