# handles句柄就是一个窗口列表，一个窗口有一个id值
# driver.window_handles         返回所有的句柄，是一个列表
# driver.current_window_handle      返回当前的句柄，是一个值
# driver.switch_to.window()         切换窗口
# driver.close()                    关闭driver


from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[3]/a').click()
print(driver.window_handles)                # ['CDwindow-1A5D8021D5DFC7DE14F83525F6E9E142']
print(driver.current_window_handle)         # CDwindow-FED23E05239CF5796C8D3F536DA0BE4F

sleep(2)
driver.quit()