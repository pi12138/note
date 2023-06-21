# 1.软件框架（software framework)
    - 通常指的是为了实现某个业界标准或完成特定基本任务的软件组件规范，也指为了实现某个软件组件规范时，提供规范所要求之基础功能的软件产品。
# 2.爬虫框架
    - 爬虫框架是实现爬虫功能的一个软件结构和功能组件集合
    - 爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫
    - scrapy
    - pyspider
    - crawley
# 3.Scrapy框架介绍
    - https://doc.scrapy.org/latest/
    - https://scrapy-chs.readthedocs.io/zh_CN/latest/index.html

    - 安装：pip install Scrapy
        - 可能安装不成功，因为scrapy有其他的依赖库，需要先安装scrapy的依赖库


# 4.scrapy概述
    - https://www.cnblogs.com/kongzhagen/p/6549053.html
    - 包含各个部件
    - "5+2"结构
    - ScrapyEngine: 神经中枢，大脑，核心，控制所以模块的数据流，根据条件触发事件，不需要用户来修改
    - Scheduler调度器：引擎发来的request请求，调度器需要处理，然后交换引擎，对所有爬取请求进行调度管理，不需要用户来修改
    - Downloader下载器：把引擎发来的requests发出请求，得到response，根据请求下载网页，不需要用户来修改
    - Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接；解析Downloader返回的响应(Response)，产生爬取项(scrapy item)，产生额外的爬取请求(Request)
    - ItemPipeline：详细处理Item；以流水线方式处理Spider产生的爬取项，由一组操作顺序组成，类似流水线，每个操作是一个ItemPipeline类型
        - 可能的操作包括：清理，检验和查重爬取项中的HTML数据，将数据存储到数据库
    - DownloaderMiddleware下载中间件：自定义下载的功能扩展组件，用户可以编写配置代码
        - 目的：实施Engine，Schedule，和Downloader之间进行用户可配置的控制
        - 功能：修改，丢弃，新增请求或者响应
    - SpiderMiddleware爬虫中间件:对Spider的功能扩展组件
        - 目的：对请求和爬取项的再处理
        - 功能：修改，丢弃，新增请求或爬取项
        
    - 各模块详细用处
        - Spider模块类似于框架入口
        - ItemPipeline模块类似于框架出口
        - Engine、Downloader、Scheduler三个模块是框架已有实现，会自动完成它们的功能不需要用户自己编写
        - Spider、ItemPipeline 模块需要用户编写(配置)
        - Spider模块提供整个框架需要访问的url链接，同时要解析从网络上获得的内容
        - ItemPipeline模块负责对提取的信息进行后处理


    - 爬虫项目大概流程：
        - 1.新建项目(建立一个Scrapy爬虫工程)
            - 示例：
                    scrapy startproject scrapy_test01
                - 生成的工程目录：    
                    scrapy_test01/ -----------> 外层目录
                        scrapy.cfg      ------> 部署Scrapy爬虫的配置文件
                        scrapy_test01/  ------> scrapy框架的用户自定义python代码
                            __init__.py   ----> 初始化脚本
                            item.py       ----> Items代码模板(继承类)
                            middlewares.py----> Middlewares代码模板(继承类)
                            pipelines.py  ----> Pipelines代码模板(继承类)
                            settings.py   ----> Scrapy爬虫的配置文件
                            spiders/      ----> Spiders代码的模板目录(继承类)
                                __init__.py --> 初始文件，无需修改
                                __pycache__/--> 缓存目录，无需修改
         
        - 2.在工程中产生一个Scrapy爬虫
            - 示例：
                    scrapy genspider test01 www.baidu.com
                - 在spiders/目录下新生成了一个test01.py文件
                - 内容见test01.py

        - 3.配置产生的spider爬虫，修改test01.py，使其能实现我们的要求
                - 有时会用到生成器，为什么要有生成器，生成器相比一次列出所有内容的优势
                    - 更节省存储空间
                    - 响应更加迅速
                    - 使用更加灵活

        - 4. 运行爬虫，获取网页
            - 示例：
                    scrapy crawl test01 
    - Scrapy 爬虫的使用步骤
        - 1.创建一个工程和Spider模板
        - 2.编写Spider
        - 3.编写Item Pipeline
        - 4.优化配置策略

    - Scrapy 爬虫的数据类型 
        - Request类 向网络上提交请求的内容
            - class scrapy.http.Request()
            - Request对象表示一个http请求
            - 由Spider生成，由Downloader执行
                |属性或方法|说明|
                |.url|Request请求对应的url地址|
                |.method|对应的请求方法，"GET","POST"等|
                |.headers|字典类型风格的请求头|
                |.body|请求内容主体，字符串类型|
                |.meta|用户添加的扩展信息，在Scrapy内部模块中传递信息使用|
                |.copy()|复制该请求|
        - Response类 表示从网络中爬取内容的封装类
            - class scrapy.http.Response()
            - Response对象表示一个HTTP响应
            - 由Downloader生成，由Spider处理
                |属性或方法|说明|
                |.url|Response对应的url地址|
                |.status|HTTP状态码，默认为200|
                |.headers|Response对应的头部信息|
                |.body|Response对应的内容信息，字符串类型|
                |.flags|一组标记|
                |.request|产生Response类型对应的Request对象|
                |.copy()|复制该请求|
        - Item类 由Spider产生的信息封装的类     
            - class scrap.http.Item()
            - Item对象表示一个从HTML页面中提取的信息内容
            - 由Spider生成，由Item Pipeline处理
            - Item类似一个字典类型，可以按照字典类型操作
    
    - Scrapy爬虫提取信息的方法
        - Scrapy爬虫支持多种HTML信息提取方法
            - Beautiful Soup
            - lxml
            - re
            - Xpath Selector
            - Css Selector
    
    - CSS Selector的基本使用
        - <HTML>.css('tag_name::attr(attr_name)').extract()
            tag_name:标签名
            attr_name:属性名
    
    - 配置并发连接选项
        - settings.py文件
                |选项|说明|
                |CONCURRENT_REQUESTS|Downloader最大并发请求下载量，默认为32|
                |CONCURRENT_ITEMS|Item Pipeline最大并发Item处理数量，默认为100|
                |CONCURRENT_REQUESTS_PER_DOMAIN|每个目标域名最大的并发请求数量，默认为8|
                |CONCURRENT_REQUESTS_PER_IP|每个目标IP最大的并发请求数量，默认为0，非0有效|
    
    - scrapy模块介绍
        - ItemPipeline
            - 对应的是pipelines文本
            - 爬虫提取出的数据存入item后，item中保存的数据需要进一步处理，比如清洗，去重，存储等
            - process_item():
                - spider 提取出来的item作为参数传入，同时传入的还有spider
                - 此方法必须实现
                - 必须返回一个Item对象，被丢弃的item不会被之后的pipeline处理
            - __init__:构造函数
                - 进行一些必要的参数初始化
            - open_spider(spider):
                - spider对象被开启的时候调用
            - close_spider(spider)
                - 当spider对象被关闭时调用
            
        - spider
            - 对应的是文件夹spiders下的文件
            - __init__：初始化爬虫名称，start_url列表
            - start_requests:生成Requests对象交给Scrapy下载并返回response
            - parse：根据返回的response解析出相应的item，item自动进入pipeline；如果需要，解析出url，url自动交给requests模块，一直循环下去
            - start_request:此方法仅能被调用一次，读取start_urls内容并启动循环过程
            - name：设置爬虫名称
            - start_urls:设置开始第一批爬取的url
            - allow_domains:spider允许爬取的域名列表
            - start_request(self)：只允许调用一次
            - parse：
            - log:日志记录

    - 中间件(DownloaderMiddlewares)
        - 中间件是位于引擎和下载器之间的的一层组件
        - 可以有很多个，被按照顺序加载执行
        - 作用是对发出的请求和返回的结果进行预处理
        - 在middlewares文件中
        - 需要在settings中设置以便生效
        - 一般情况下一个中间件完成一项功能
        - 必须实现以下一个或者多个方法：
            - process_request(self, request, spider)
                - 在request通过的时候被调用
                - 必须返回None或者Response或者Request或者raise IgnoreRequest
                - None：scrapy将继续处理该request
                - Request：scrapy会停止调用process_request并重新调度返回的request
                - Response：scrapy将不会调用其他process_request或者process_exception,直接将该Response作为结果返回，同时会调用process_response()函数
            - process_response(self, request, response, spider)
                - 跟process_request大同小异
                - 每次返回结果时自动调用
                - 可以有多个，按顺序调用

# 5.Scrapy命令行
    - Scrapy是为了持续运行设计的专业爬虫框架，提供操作的Scrapy命令行
    - scrapy命令行格式
            scrapy <command> [options] [args]
            
            <command>: scrapy命令
    
    - scrapy常用命令
            |命令|说明|格式|
            |startproject |创建一个新的工程|scrapy startproject <name>[dir]|
            |genspider|创建一个爬虫|scrapy genspider [options]<name>[domain]|
            |settings|获得爬虫配置信息|scrapy settings [options]|
            |crawl|运行一个爬虫|scrapy crawl <spider>|
            |list|列出工程中的所有爬虫|scrapy list|
            |shell|启动URL调试命令行|scrapy shell [url]|

    - 为什么Scrapy采用命令行创建和运行爬虫？
        - 命令行(不是图形化界面)更容易自动化，适合脚本控制
        - 本质上，Scrapy是给程序员使用的，功能(而不是界面)更重要

# 6.Scrapy终端（Scrapy shell）
    - Scrapy终端是一个交互终端，供您在未启动spider的情况下尝试及调试您的爬取代码。其本意是用来测试提取数据的代码，不过您可以将其作为正常的Python终端，在上面测试任何的Python的代码。
    
    该终端是用来测试XPath或CSS表达式，查看他们的工作方式及从爬取的网页中提取的数据。在编写您的蜘蛛时，该终端提供了交互性测试您的表达式代码的功能，免去了每次修改后运行蜘蛛的麻烦。

    一旦熟悉了Scrapy终端后，您会发现其在开发和调试蜘蛛时发挥的巨大作用。

    如果您安装了IPython中，Scrapy终端将使用IPython的（替代标准的Python终端）。 IPython的终端与其他相比更为强大，提供智能的自动补全，高亮输出，及其他特性。

    - 终端启动
        - 可以您使用shell来启动Scrapy终端：
            scrapy shell <url>
            <url> 是您要爬取的网页的地址。
    
# 7.scrapy框架 和 requests库的比较
    - 相同点：
        - 两者都可以进行页面请求和爬取，Python爬虫的两个重要技术路线
        - 两者可用性都好，文档丰富，入门简单
        - 两者都没有处理js，提交表单，应对验证码等功能(可扩展)
    - 不同：
        
            |requests               |scrapy                  |
            |页面级爬虫              |网站级爬虫               |
            |功能库                  |框架                    |
            |并发性考虑不足，性能较差 | 并发性好，性能较高       |
            |重点在于页面下载         |重点在于爬虫框架         |
            |定制灵活                |一般定制灵活，深度定制困难|
            |上手十分简单            |入门稍难                 |
    - 选取使用：
        - 非常小的需求，requests库
        - 不太小的需求，Scrapy框架
        - 定制程度很高的需求(不考虑规模)，自搭框架，requests > scrapy