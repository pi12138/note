'''
正则中文匹配
'''

import re

str1 = u'你好，世界'
rules = r'[\u4e00-\u9fa5]+'

pattern = re.compile(rules)

content = pattern.search(str1)

print(content)
