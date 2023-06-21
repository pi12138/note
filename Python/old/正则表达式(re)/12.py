import re


title = u'<div>name</div><div>age</div>'

# 贪婪匹配
p1 = re.compile(r"<div>.*</div>")

# 非贪婪匹配
p2 = re.compile(r"<div>.*?</div>")

rst1 = p1.search(title)
rst2 = p2.search(title)

print(rst1.group())
print(rst2.group())