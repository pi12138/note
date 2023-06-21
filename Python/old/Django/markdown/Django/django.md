# 1.虚拟环境
	- mkvirtualenv [env_name]	创建虚拟环境
	- rmvirtualenv	[env_name]	删除虚拟环境
	- workon [env_name]			进入虚拟环境
	- deactivate				退出虚拟环境

	- 显示已经创建的虚拟环境: workon, lsvirtualenv

# 2. django项目流程
	- (1) 
		- django-admin startproject [项目名]		创建项目
		- python manage.py startapp [应用名]		创建应用

	- (2)
		- 将[应用名]注册到settings.py 文件的 INSTALLED_APPS中
		- 如果需要更改数据库在setting.py 文件的DATABASES中更改
		- 在models.py 中编写模型类

	- (3)
		- python manage.py makemigrations		根据模型类生成迁移文件
		- python manage.py migrate				执行迁移文件
		- python manage.py shell				可以在shell中测试数据操作

	- (4)
		- python manage.py runserver [ip:port]	运行项目

	- (5)
		- python manage.py createsuperuser		创建一个管理员账户，根据提示创建

# 3. admin的使用
	- 127.0.0.1:8000/admin

	- admin.py 文件中进行注册操作
		- admin.site.register(模型类) 或者 admin.site.register(模型类,admin类)

# 4.MVT
	- 视图View :接收请求，逻辑处理，调用数据，输出响应
		- 配置url：在自己的应用中匹配正则url(正则表达式，视图名称)
			例如： (r'^\d+$', views.show)

	- 模型Model:负责与数据库交互
		- 面向对象：模型对象，列表
		- 在models.py 中定义模型类
			- 指定属性及属性的类型，以确定表结构(类名即为表名，属性为列名)
			- 迁移在数据库中生成表
			- 后台管理：django封装好的后台管理,数据库表的增删改查
				步骤：
					1. 创建管理员 python manage.py createsuperuser
					2. 启动服务器 python manage.py runserver
					3. 在admin.py 中注册模型类
					4. 127.0.0.1:8000/admin 登录到后台，可以进行数据库表的相关操作

	- 模板Template:负责呈现内容到浏览器
		- 加载：读取文件内容到内存
		- 渲染：填坑(将文件内容进行再次处理，比如传参)

# 5.django项目基本开发过程
	- step1:创建虚拟环境		mkvirtualenv [虚拟环境名]
	- step2:安装django		
	- step3:创建项目			django-admin startproject [项目名]
	- step4:创建应用，在setting.py中添加应用
	- step5:根据设计的数据库表结构在models.py中定义模型类
	- step6:定义视图
	- step7:配置url
	- step8:创建模板，在setting.py中添加模板路径
	