# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/26 16:01
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium.webdriver.remote.webdriver import WebDriver

from Project.企业微信.PageObject实战1.PO.Register_PO import Register


class Login():
    def __init__(self,driver:WebDriver):            # 复用上一个PO的driver，driver:WebDriver指定为WebDriver类型后，可以使用find方法
        self._driver = driver
    def scan(self):
        pass
    def click_register(self):
        # 点击立即注册
        self._driver.find_element_by_css_selector('.login_registerBar_link').click()
        return Register(self._driver)
