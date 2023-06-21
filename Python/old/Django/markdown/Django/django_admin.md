# Admin站点

- admin站点默认是英文版的，如果想要将其变成中文版

  - 设置一下两项

    ```python
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    # 改为
    LANGUAGE_CODE = 'zh-hans'
     
    TIME_ZONE = 'Asia/Shanghai'
    ```

  - 或者，设置中间件，添加`django.middleware.locale.LocaleMiddleware` 到` MIDDLEWARE_CLASSES` 设置中，并确保它在`django.contrib.sessions.middleware.SessionMiddleware` 之后。 

	- 在使用django-admin startproject [project_name] 创建项目时，默认admin被启用，在setting.py --> INSTALLED_APPS中
	
	- 使用步骤：
		- step1：创建管理员的用户名和密码
				 python manage.py createsuperuser
				 按照提示填写内容
		- step2：将models.py 中定义的模板在admin.py 中注册后，就可以在后台中维护模型的数据
				 from models import *
				 admin.site.register(class_name)
		- step3: 运行服务器后，使用 xxx/admin 进入后台管理界面
	
	### 1.备注： 创建管理员后 管理员信息保存在表 auth_user 中

# ModelAdmin对象
	- ModelAdmin 类是模型在Admin界面的表现形式
	- 通过重写admin.ModelAdmin 的属性自定义显示效果，属性主要分为列表页和增加修改页两部分
	
	- 使用方法：定义一个类，继承于admin.ModelAdmin，注册模型是使用这个类
		- 方法1：注册参数
			```
			class HeroAdmin(admin.ModelAdmin):
				.....
	
			admin.site.register(HeroInfo, HeroAdmin)
			```
		- 方法2：注册装饰器
			```
			@admin.register(HeroInfo)
			class HeroAdmin(admin.ModelAdmin)
			```
	
	- 列表页选项：
		- list_display 
			- 出现列表中显示的字段
			- 在列表中，可以是字段名称，也可以是方法名称(例如：处理性别)，但是方法名称默认不能排序
			- 在方法中可以使用format_html()输出html内容
			```
			class HeroAdmin(admin.ModelAdmin):
				list_display = ['hname', 'hcontent']
		- list_filter
			- 右侧栏过滤器，可以选择对某些属性进行过滤
			```
			class HeroAdmin(admin.ModelAdmin):
				list_filter = ['hname']
			```
		- list_per_page
			- 规定每页显示多少项，默认设置为100
		- search_fields
			- 设置搜索框，列表类型，表示在这些字段上搜索
			- 如果字段的返回结果为一个对象，查询时需要查询关联对象中的字段，使用双下划线分隔__
			```
			search_fields = ['hname']
			```
	
	- 增加与修改页选项
		- fields
			- 显示字段顺序，如果使用元组表示显示到一行上
			```
			class HeroAdmin(admin.ModelAdmin):
				fields = [('hname', 'hcontent')]
			```
		- fieldsets
			- 分组显示
			```
			fieldsets = (
				('base': {'fields': ('hanme')})
				('other': {'fields': ('hcontent')})
				)
			```
		- fields 和 fieldsets两者选一

# InlineModelAdmin对象
	- 表示在模型的添加，修改页面嵌入"关联模型"的添加或修改
	- 子类TabularInline:表示以表格的形式嵌入
	- 子类StackedInline：表示以块的形式嵌入
		```
		class HeroInline(admin.TabularInline):
			model = HeroInfo
	
		class BookAdmin(admin.ModelAdmin):
			inlines = [HeroInline]
		```