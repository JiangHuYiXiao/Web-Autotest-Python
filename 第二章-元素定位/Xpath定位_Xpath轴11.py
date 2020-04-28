# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 8:28
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# Xpath轴（Axes）定位：
# 1、parent选择当前节点的上一层父节点
    # //img[@alt='div1']/parent::div                  div1的上一层div

# 2、child选择当前节点下层的所有子节点
    # //img[@alt='div1']/child::div                  div1的下层的所有div

# 3、ancestor选择当前节点的所有上层节点
    # //img[@alt='div1']/ancestor::div                  div1的上一层div

# 4、通过text()函数定位
# 通过text()函数可以定位到元素文本包含某些关键内容的页面元素
    # //a[text()="百度一下"]
    # //a[.="百度一下"]
    # //a[contains(.,”百度”)]
    # //a[contains(text(),”百度”)]
    # //a[contains(text(),”百度”)]/preceding::div
    # //a[contains(百度”)]/..


# 5、descendant：选择当前节点所有下层的节点(子、孙)
    # //div[@name=‘div2’]/descendant::img

# 6、following：选择当前节点之后显示的所有节点
    # //div[@id=‘div1’]/following::img

# 7、following-sibling：选择当前节点后续所有兄弟节点
    # //a[@href=‘http://www.sogou.com’]/following-sibling::input

# 8、preceding：选择当前节点前面的所有节点
    # //img[@alt=‘div2-img2’]/preceding::div

# 9、Preceding-sibling：选择当前节点前面的所有亲兄弟节点
    # //input[@value=‘查询’]/preceding-sibling::a[1]

