# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/26 11:09
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium.webdriver.remote.webdriver import WebDriver
import time

class Register():
    def __init__(self,driver:WebDriver):
        self._driver = driver
    def send_content(self):
        # 企业名称
        self._driver.find_element_by_css_selector('#corp_name').send_keys('江湖一笑')
        # 管理员姓名
        self._driver.find_element_by_css_selector('#manager_name').send_keys('江湖一笑')
        # 手机号
        self._driver.find_element_by_css_selector('#register_tel').send_keys('18270717372')
        time.sleep(5)
        self._driver.quit()
        return True


