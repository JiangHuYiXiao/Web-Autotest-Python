# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/13 7:51
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 有的时候我们需要操作当前页面之下或者之右的元素时候，是需要拖拽当前页面往下或者往右的。

# 方法1：滚动元素可见
# driver.execute_script("return arguments[0].scrollIntoView();",targent_elem)
# 0：指的是第一个参数
# targent_elem:指的是定位出来的一个页面元素

# 方法2：
# driver.execute_script("scroll(0,2400)")    # 0,指的是X轴，2400指的是Y轴
# driver.execute_script（"window.scrollBy()"）
# driver.execute_script("window.scrollBy(0,500)")向下滚动500个像素
# window.scrollBy(0,-500)　　 向上滚动500个像素
# driver.execute_script("window.scrollBy(500,0)")　　   向右滚动500个像素
# window.scrollBy(-500,0)　　 向左滚动500个像素

# 示例1：
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(6)           # 设置超时等待时间
driver.maximize_window()
driver.get('http://news.baidu.com')
# 不生效
# tech_Ele = driver.find_element_by_css_selector('#tiyu > div.column-title-home > div.column-title-border > h2 > a')
# driver.execute_script("arguments[0].scrollIntoView();",tech_Ele)

# 多次重复，每次拉动1000
# driver.execute_script("scroll(0,1000)")    # 0,指的是X轴，100指的是Y轴
# sleep(1)
# driver.execute_script("scroll(0,2000)")    # 0,指的是X轴，100指的是Y轴
# sleep(1)
# driver.execute_script("scroll(0,3000)")    # 0,指的是X轴，100指的是Y轴
# sleep(1)
# driver.execute_script("scroll(0,4000)")    # 0,指的是X轴，100指的是Y轴

# 使用循环
shu = 1000
print(type(shu))
for i in range(4):
    driver.execute_script("scroll(0,"+str(shu)+")")
    shu += 1000
    sleep(1)
driver.find_element_by_css_selector('#tiyu > div.column-title-home > div.column-title-border > h2 > a').click()
sleep(2)
driver.quit()
