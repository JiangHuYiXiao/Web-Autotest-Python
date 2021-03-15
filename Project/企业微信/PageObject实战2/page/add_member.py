# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/3/8 8:30
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class Add_Member():
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def save_contacts(self):
        '''
        填写用户信息，保存用户信息
        :return:
        '''
        sleep(5)
        self._driver.find_element_by_css_selector('#username').send_keys('user1')
        self._driver.find_element_by_css_selector('#memberAdd_english_name').send_keys('user1')
        self._driver.find_element_by_css_selector('#memberAdd_acctid').send_keys('user1')

        self._driver.find_element_by_css_selector('#memberAdd_phone').send_keys('18270717274')
        sleep(2)
        self._driver.find_element_by_css_selector('.js_btn_continue').click()

        sleep(4)
        return True


