# Log
    - logging模块提供模块级别的函数记录日志
    - 包括四大组件
    - https://www.cnblogs.com/yyds/p/6901864.html

# 1.日志相关概念
    - 日志：需要进行i/o操作，但是i/o操作比较慢，所以一般不轻易写日志，一般用来记录关键
            内容
    - 日志级别(level):
        - 不同用户关注不同的程序信息
        - DEBUG
        - INFO
        - NOTICE
        - WARNING
        - ERROR
        - CRITICAL
        - ALERT
        - EMERGENCY
      
    - io操作=>不要频繁操作
    
    - LOG的作用
        - 调试
        - 了解软件的运行情况
        - 分析定位问题
    - 日志信息：
        - time
        - 地点
        - level
        - 内容
    - 成熟的第三方日志：
        - log4j
        - log4php
        - logging
        
# 2. logging模块
    - 日志级别：
        - 级别可以自定义
        - DEBUG
        - INFO
        - WARNING
        - ERROR
        - CRITICAL
    - 初始化/写日志实例时需要指定级别，只有当级别等于或者高于指定级别才被记录
    - 使用方式：
        - 直接使用logging模块
        - logging四大组件直接定制
# 3. logging模块级别的日志
     - 使用以下几个函数
        logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
        logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
        logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
        logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
        logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
        logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
        logging.basicConfig(**kwargs)	对root logger进行一次性配置
     - logging.basicConfig(**kwargs) 
        - 只在第一次调用时才起作用
        - 不配值logger则使用默认值
            - 输出：sys.stderr
            - 级别：WARNING
            - 格式：level:log_name:content
# 4. logging 模块的处理流程
    - 四大组件：
        - 日志器（Logger）：产生日志的一个接口
        - 处理器（Handler）：把产生的日志发送到相应的目的地
        - 过滤器（Filter）；更精细的控制那些日志输出
        - 格式器（Formatter）： 对输出信息进行格式化