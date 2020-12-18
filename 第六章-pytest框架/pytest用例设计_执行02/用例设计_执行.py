# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/1 8:32
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 1、用例设计原则：
    # 文件名以test_*.py开头或者以_test.py结尾
    # 测试类，以Test开头，并且不能带有init方法
    # 以test_开头的方法
    # 以test_开头的函数
    # package必须要有__init__.py文件
    # 断言使用assert




# 2、执行方式
    # 使用命令执行pytest用例，首先需要切换到用例所在目录
    # 用例执行方式1：pytest

    # 用例执行方式2：py.test

    # 用例执行方式3：python -m pytest

# 3、执行规则
    # 3.1、某个目录下所有的用例
        # 查找当前目录或者子目录下以test_*.py开头的或者以*_test.py结尾的文件
        # 找到文件后，在文件中找到以test开头的函数或者方法并执行
        # pytest
    # 3.2、执行某一个py文件下用例
        # pytest test_add1.py

    # 3.3.-k按关键字匹配
    # pytest -k "MyClass and not method“

    # 3.4.按节点运行
        # 运行.py模块里面的某个函数
        # pytest test_add1.py ::test_add2

        # 运行.py模块里面,测试类里面的某个方法
        # pytest test_mod.py::TestClass::test_method

    # 3.5.标记表达式，
        # >pytest -m slow   用于有标签的
        # 将运行用@ pytest.mark.slow装饰器修饰的所有测试用例，标签名为slow，标签名可以自定义，后面章节会讲自定义标记mark的功能。

    # 3.6.从包里面运行
        # >pytest --pyargs pkg.testing
        # 返将导入pkg.testing并使用其文件系统位置来查找来运行测试。

# 3、测试类
    # 多条用例时，我们可以建立测试类

# 4、用例部分执行
    # pytest -q test_add1.py
    # py.test -q test_add1.py
    # python -m pytest -q test_add1.py

# 5、pytest的用例执行顺序
    # 写在前面的就是先执行
    # 如果需要自定义顺序，可以使用pytest-ordering插件进行自定义顺序
    # 先按照pyetest-ordering  pip install pytest-ordering
    # order数字小的先执行（0-7）（-1 -7）0最新执行，-7最后执行
'''
import pytest

@pytest.mark.run(order=2)
def test_foo():
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True

'''


# 6、导出依赖包 pip freeze
# 我们在使用别人的开源的项目时候，需要导出比人项目的所有包可以使用以下命令
# pip freeze > requirements.txt
# pip install -r requirements.txt

