# 1. 几种常用提取信息工具的比较
    - 正则：很快，不好用，不用安装
    - beautifulsoup：慢，使用简单，安装简单
    - lxml：比较快，使用简单，安装简单
# 2. css选择器
    - beautifulsoup4本质上就是一个css选择器
# 3. beautifulsoup
    - 创建一个BeautifulSoup对象     soup = BeautifulSoup(html_code)
    - 格式化函数 soup.prettify() 可以补齐缺少的html标签，案例见10.py 
    
    - 四大对象：
        - Tag
        - NavigableString
        - BeautifulSoup
        - comment
    
     - Tag
        - 对应html中的标签
        - 可以通过soup.tag_name
        - 使用soup.tag_name 来查找标签，只能查找到同名标签中的第一个
        - tag三个比较重要的属性：
            - name，name可以查看标签名，返回一个str类型
            - attrs，attrs可以查看标签属性，返回一个dict类型,attrs['attr']可以查看指定属性，也可以使用attrs['attr'] = 'new_attr' 来修改属性
            - text，text可以查看标签文本内容，返回一个str
        - 案例见11.py
    
     - NavigableString
        - 对应内容值
        - 案例见12.py
    
    - BeautifulSoup
        - 表示的是一个文档的内容，大部分可以把他当作tag对象
        - 一般我们可以用soup表示
        - 案例见13.py
    
    - Comment
        - 注释内容
        - 特殊的NavigableString对象
        - 对其输出，则内容不包括注释符号
        - 案例见14.py，test04.html 

# 4. 遍历文档内容
    - contents：tag的直接子节点以列表的方式给出
    - children：直接子节点以迭代器返回
    - descendants：返回所有子孙节点 
    - string：获取tag的文本内容 ，如果tag只有一个 NavigableString类型子节点,那么这个tag可以使用 .string 得到子节点内容，如果超过一个, 返回None
    - strings 属性 获取所有内容, 返回一个generator(包括空白字符) 
    - stripped_strings 属性 获取所有内容, 返回一个generator(去除空白字符)
    - 案例见15.py，test04.html

# 5. 搜索文档对象
    - find_all(name=None, attrs={}, recursive=True, text=None, limit=None,  **kwargs)
        - 返回内容为一个list
        - name：按照那个字符串搜索，可以传入的内容为
            - 字符串
            - 正则表达式
            - 列表
        - attrs：和name一起使用标签名和标签属性匹配标签
        - kwargs:不用和name一起使用，可以用来表示属性，搜索某个或多个带有指定属性的标签
            - find_all(id='text')   可以查找所有带有"id='text'" 的标签
            - 上面代码功能和这个一样 find_all("", {'id':'text'})
        - text：使用文本内容去匹配标签，返回的是文本内容，可以使用len()函数得到标签数量
        - 案例见16.py
        - 案例见17.py, test05.html

# 6.css选择器
    - 使用soup.select(),返回一个列表
    - 查找方式：
        - 通过标签名称：soup.select('tag_name')
        - 通过类名：soup.select('.class_name')
        - 通过id：soup.select('#id_name')
        - 组合查找：soup.select('div.class_name')
        - 属性查找：soup.select('tag_name[attrs_name = "attrs_value"]')
    - 获取tag内容：tag_name.get_text()返回字符串，自动过滤标签
    - 案例见18.py，test05.html