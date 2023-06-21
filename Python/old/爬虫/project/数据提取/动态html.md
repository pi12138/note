# 1.动态html介绍
    - javascript
    - jQuery(javascript框架)
    - Ajax
    - DHTML

    - python采集动态数据
        - 从javascript代码入手采集
        - python第三方库允许javascript，直接采集在浏览器看到的页面

# 2.Selenium + PhantonJS
    - 最新版的selenium已经不支持phantonjs 如果想使用推荐按照pip install selenium==2.48.0
    - Selenium:web自动化测试工具
        - 自动加载页面
        - 获取数据
        - 截屏
        - 安装：pip install selenium
        - 官网：https://selenium-python.readthedocs.io/index.html
    - PhantomJS(幽灵浏览器)
        - 基于webkit的无界面的浏览器
        - 官网：http://phantomjs.org/download.html
    
    - Selenium库里有一个WebDriver的API
    - WebDriver可以跟页面上的元素进行各种交互，用它可以进行爬取
    - 案例见19.py

- Python+Selenium WebDriver API：浏览器及元素的常用函数及变量整理总结
    - https://www.cnblogs.com/yufeihlf/p/5764807.html

    - 调用说明：
        driver.属性值
        
        变量说明：
        1.driver.current_url：用于获得当前页面的URL
        2.driver.title：用于获取当前页面的标题
        3.driver.page_source:用于获取页面html源代码
        4.driver.current_window_handle:用于获取当前窗口句柄
        5.driver.window_handles:用于获取所有窗口句柄

# 3. Selenium + chrome
    - chrome + chromedriver
        - 下载安装chrome：下载+安装
        - 下载chromedriver：百度

    - Selenium操作主要分两大类：
        - 得到UI元素
            - find_element_by_id
            - find_elements_by_name
            - find_elements_by_xpath
            - find_elements_by_link_text
            - find_elements_by_partial_link_text
            - find_elements_by_tag_name
            - find_elements_by_class_name
            - find_elements_by_css_selector
        - 基于UI元素操作的模拟
            - 单击
            - 右键
            - 拖拽
            - 输入
            - 可以通过导入ActionsChains类来做到
        
        - 案例见20.py

        - https://blog.csdn.net/u010986776/article/details/79266448