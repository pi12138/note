'''
对于复杂的模式，请使用 re 模块中的 sub() 函数。为了说明这个，假设你想将形
式为 11/27/2012 的日期字符串改成 2012-11-27 。示例如下：
sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字
比如 \3 指向前面模式的捕获组号。
'''
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

print(text)
print(new_text)

'''
如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。比如：
'''

pat = re.compile(r'(\d+)/(\d+)/(\d+)')

new_text2 = pat.sub(r'\3-\1-\2', text)

print(new_text2)


'''
对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：

'''

from calendar import month_abbr

def change_date(date):
    mon_name = month_abbr[int(date.group(1))]
    return '{0} {1} {2}'.format(date.group(2), mon_name, date.group(3))

new_text3 = pat.sub(change_date, text)
print(new_text3)

'''
一个替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回
的对象。使用 group() 方法来提取特定的匹配部分。回调函数最后返回替换字符串。
如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn()
来代替。比如：
'''
new_text4, n = pat.subn(change_date, text)
print(new_text4)
print(n)

'''
讨论
关于正则表达式搜索和替换，上面演示的 sub() 方法基本已经涵盖了所有。其实
最难的部分就是编写正则表达式模式，这个最好是留给读者自己去练习了。

'''