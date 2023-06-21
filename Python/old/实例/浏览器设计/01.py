'''
模块webbrowser
'''

import webbrowser

url = "https://www.baidu.com/"
# webbrowser.open(url, new=0, autoraise=True)
# new: 0/1/2
# 0：同一浏览器窗口打开
# 1：打开浏览器新的窗口，
# 2：打开浏览器窗口新的tab
# autoraise=True:窗口自动增长

webbrowser.open(url)

webbrowser.open_new(url)

webbrowser.open_new_tab(url)