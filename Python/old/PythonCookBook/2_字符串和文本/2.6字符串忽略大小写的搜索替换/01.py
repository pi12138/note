"""
问题：
	以忽略大小写的方式搜索与替换文本字符串
解决方案：
	为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供
re.IGNORECASE 标志参数。比如：
"""

import re

text = "UPPER PYTHON, lower python, Mixed Python"

result = re.findall('python', text, flags=re.IGNORECASE)


