# handles句柄就是一个窗口列表，一个窗口有一个id值
# driver.window_handles         返回所有的句柄，是一个列表
# driver.current_window_handle      返回当前的句柄，是一个值
# driver.switch_to.window()         切换窗口
# driver.close()                    关闭driver


# 示例1：返回所有句柄和当前句柄
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.find_element_by_xpath('//*[@id="header-link-wrapper"]/li[3]/a').click()          # 贴吧
print(driver.window_handles)                # ['CDwindow-1A5D8021D5DFC7DE14F83525F6E9E142']
print(driver.current_window_handle)         # CDwindow-FED23E05239CF5796C8D3F536DA0BE4F
sleep(2)
driver.get('http://news.baidu.com')

print(driver.window_handles)
print(driver.current_window_handle)
sleep(2)

driver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a').click()
sleep(2)
# hands存储所有句柄
hands = driver.window_handles
# 关闭百度句柄
driver.close()          # 直接这么关闭报错，需要在这之前把所有的句柄通过变量存下来
driver.switch_to.window(hands[1])
print(driver.title)
print(driver.window_handles)
print(driver.current_window_handle)
sleep(2)

driver.quit()