# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/12/23 9:37
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7



# allure是一个生成测试报告的文件
# 下载allure-commandline-2.13.1.zip地址：https://github.com/allure-framework/allure2/releases/tag/2.13.1
# 还需要安装allure-pytest第三方库

# 生成测试报告：allure generate ./
# 打开测试报告：不能直接双击index.html，需要使用命令: allure open 报告目录/
# 生成json文件：pytest --alluredir ./report


# 使用allure提供的一些API:
# 添加操作步骤说明，插入图片、插入视频、添加case链接、添加bug链接、定义stories、fixture