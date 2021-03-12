# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/3/12 8:46
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
1、公共方法需要替代页面提供的服务，比如我们这个案例中的index中的goto_login方法和goto_register方法，替代了页面的登录、注册服务
2、不要暴露页面的细节（比如我们在index中把元素的定位放到一个方法中且在case中我们直接调用goto方法）这样我们以后页面的定位元素发生了改变只需要修改对应的PO，不需要修改case
3、PO和断言分离，断言在case中
4、一个方法需要返回到另一个PO页面，针对于页面之间有交互的时候，比如我们例子中的index中的return Register（self._driver）
5、不要去实现整个页面的功能进行创建PO
6、针对不同结果创建（不做要求）
'''
