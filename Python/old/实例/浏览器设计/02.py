'''
用pyqt5打开网页
'''

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
app = QApplication(sys.argv)
browser = QWebEngineView()
browser.load(QUrl("http://www.baidu.com/"))
browser.show()
app.exec_()
