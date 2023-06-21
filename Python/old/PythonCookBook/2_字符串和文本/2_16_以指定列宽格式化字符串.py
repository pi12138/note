"""
问题
    你有一些长字符串，想以指定的列宽将它们重新格式化。
解决方案
    使用 textwrap 模块来格式化字符串的输出。比如，假如你有下列的长字符串：
"""

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."


print(textwrap.fill(s, 70)) 
# > Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
#   not around the eyes, don't look around the eyes, look into my eyes,
#   you're under.

print(textwrap.fill(s, 40))
# > Look into my eyes, look into my eyes,
#   the eyes, the eyes, the eyes, not around
#   the eyes, don't look around the eyes,
#   look into my eyes, you're under.

# 首行缩进
print(textwrap.fill(s, 40, initial_indent="  "))
# >   Look into my eyes, look into my eyes,
#   the eyes, the eyes, the eyes, not around
#   the eyes, don't look around the eyes,
#   look into my eyes, you're under.

# 首行悬挂
print(textwrap.fill(s, 40, subsequent_indent="  "))
# > Look into my eyes, look into my eyes,
#     the eyes, the eyes, the eyes, not
#     around the eyes, don't look around the
#     eyes, look into my eyes, you're under.


""" 
讨论
    textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端
大小的时候。你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。比如：
"""

import os 

print(os.get_terminal_size().columns)       # > 126


"""
fill() 方 法 接 受 一 些 其 他 可 选 参 数 来 控 制 tab， 语 句 结 尾 等。参 阅 textwrap.TextWrapper 文档 获取更多内容。
""" 