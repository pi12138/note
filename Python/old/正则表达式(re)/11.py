import re

title = u"世界 你好, hello world"

p = re.compile(r'[\u4e00-\u9fa5]+')

rst = p.findall(title)

print(rst)