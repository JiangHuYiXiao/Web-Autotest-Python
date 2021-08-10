# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/10 9:19
# @Software       : Python_study
# @Python_verison : 3.7
import yaml


# 将python数据转换成yaml文件
stream = open('test.yaml','w')
data = [1, 2, 'aaa',{'key1':'value1'}]
yaml.dump(data=data,stream=stream)
print(yaml.dump(data))


# 将yaml数据转换成python文件

'''
-表示一个数组
缩进用空格，不要用tab
字典使用key:value

'''
stream1 = '''
- 
 - 2
 - aaa
- 
 key1: value1
  '''
print(yaml.load(stream=stream1, Loader =yaml.FullLoader))
# [[2, 'aaa'], {'key1': 'value1'}]

# 列表嵌套字典
stream2 = '''
- 
 - 2
 - aaa
 - key1: value1
  '''
print(yaml.load(stream=stream2, Loader =yaml.FullLoader))
# [[2, 'aaa', {'key1': 'value1'}]]

# 字典嵌套列表
stream2 = '''
companies:
    -
     id: 1
     name: company1
     price: 200W
'''

print(yaml.load(stream=stream2, Loader =yaml.FullLoader))

# 复合结构
stream3 ='''
languages:
  - Ruby
  - Perl
  - Python 
websites:
  YAML: yaml.org 
  Ruby: ruby-lang.org 
  Python: python.org 
  Perl: use.perl.org
'''
print(yaml.load(stream=stream3, Loader =yaml.FullLoader))

