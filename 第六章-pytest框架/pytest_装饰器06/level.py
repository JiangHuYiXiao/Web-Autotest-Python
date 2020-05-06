# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/6 9:08
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import pytest
level = 4
test_level = pytest.mark.skipif(level==4,reason='level 4 is skip')               # 如果python版本大于3.6则跳过
