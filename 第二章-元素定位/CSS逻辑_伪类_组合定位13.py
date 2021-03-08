# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 9:19
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# ******CSS其他属性我们直接写=，只有id为#，class为.******
# 1、逻辑运算符定位，不仅CSS可以使用，Xpath也可以使用
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("span[class='bg.s_ipt_wr' and id = 's_kw_wrap']/input").send_keys('selenium')
driver.find_element_by_xpath("span[class='s_btn_wr.bg' and id = 's_btn_wr']/input").click()
sleep(2)
driver.quit()


# 2、正则表达式定位，不仅CSS可以使用，Xpath也可以使用
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("span[class^='bg' and id = 's_kw_wrap']/input").send_keys('selenium')          # 以bg开始
driver.find_element_by_xpath("span[class$='ipt_wr' and id = 's_btn_wr']/input").click()          # 以ipt_wr结尾
driver.find_element_by_xpath("span[class*='bg' and id = 's_btn_wr']/input").click()          # 包含bg
sleep(2)
driver.quit()

# 3、组合定位
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('form.fm>span#s_kw_wrap>input[autocomplete="off"]').send_keys('selenium')
driver.find_element_by_css_selector('form#form>span#s_btn_wr>input[type="submit"]').click()
driver.find_element_by_css_selector('input#kw.s_pt').click()
sleep(2)
driver.quit()

# 4、伪类定位

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_css_selector('li#li1:first-child').send_keys('selenium')     # 第一个子元素
driver.find_element_by_css_selector('li#li1:nth-child(2)').send_keys('selenium')    # 第二个子元素
driver.find_element_by_css_selector('li#li1:last-child').send_keys('selenium')      # 最后一个子元素
driver.find_element_by_css_selector('input:enable').click()
driver.find_element_by_css_selector('input:focus').click()
driver.find_element_by_css_selector('input:checked').click()        # 选中的
driver.find_element_by_css_selector('input:not([id])').click()
sleep(2)
driver.quit()


# 综合：Xpath的定位功能更强大，CSS虽然查询速度快，但是有的浏览器不支持CSS定位，我们在自动化测试中使用Xpath更多点。