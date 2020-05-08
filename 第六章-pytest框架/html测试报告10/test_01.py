# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/8 9:10
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
pytest-HTML 是一个插件， pytest 用于生成测试结果的 HTML 报告。
pip 安装
> pip install pytest-html
执行方法
> pytest --html=report.html
此方法生成的报告， css 是独立的，分享报告的时候样式会丢失，为了更好的分享发邮件展示报告，可以把 css 样式合并到 html 里。
pytest --html=report.html --self-contained-html

'''
import pytest
def test_01():
    print('用例1')
def test_02():
    print('用例2')
def test_03():
    print('用例3')

if __name__ =='__main__':
    pytest.main()