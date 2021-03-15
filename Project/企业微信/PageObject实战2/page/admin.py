# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/3/8 8:29
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Project.企业微信.PageObject实战2.page.add_member import Add_Member

class Admin():
    def __init__(self):
        chrome_option = Options()
        chrome_option.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=chrome_option)
        self._driver.maximize_window()
        self._driver.get('https://work.weixin.qq.com')


    def goto_add_member(self):
        '''
        点击添加成员，跳转到添加成员列表页面
        :return:Add_Member()
        '''
        sleep(3)
        self._driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        return Add_Member(self._driver)



    def goto_import_member(self):
        pass

