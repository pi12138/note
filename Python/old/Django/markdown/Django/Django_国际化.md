# `国际化和本地化`

- 使用步骤

    - 配置`settings`文件

        ```python
        MIDDLEWARE_CLASSES = (
            ...
            'django.middleware.locale.LocaleMiddleware',
        )
         
         
        LANGUAGE_CODE = 'en'
        TIME_ZONE = 'UTC'
        USE_I18N = True
        USE_L10N = True
        USE_TZ = True
         
        LANGUAGES = (
            ('en', ('English')),
            ('zh-cn', ('中文简体')),
            ('zh-tw', ('中文繁體')),
        )
         
        #翻译文件所在目录，需要手工创建
        LOCALE_PATHS = (
            os.path.join(BASE_DIR, 'locale'),
        )
         
        TEMPLATE_CONTEXT_PROCESSORS = (
            ...
            "django.core.context_processors.i18n",
        )
        ```

    - 在视图中标识需要翻译的文本(使用`ugettext()`函数标识)

        ```python
        from django.utils.translation import ugettext
        from django.http import HttpResponse
        
        def test_language(request):
            output = ugettext("Welcome to my site!")
            return HttpResponse(output)
        ```

    - 在模板中标识需要翻译的文本(使用`{% trans %}或 {% blocktrans %}xxxxx{%endblocktrans%}`)

        - **注意：首先你要在模版的顶部加载`{% load i18n %}`。**

        ```python
            {% load i18n %}
            <h1>{% trans "xxxxxxxxxx" %}</h1>
            {% blocktrans %}This string will have {{ value }} inside. {% endblocktrans %}
        ```

    - 本地化

        - 一旦标记好需要翻译的文本（也就是国际化）后，就需要进行本地化，也就是创建翻译用的语言文件。
        - 运行`python manage.py makemessages -l zh-hans`(或者`django-admin makemessages -l zh-hans`,该命令需要到指定模块下执行)

        ```shell
        python manage.py makemessages -l zh-cn 	// 中文简体
        python manage.py makemessages -l en     // 英文
        ```

        - ### 注意：在Windows下，需要提前安装GNU gettext工具！

        - 执行完该命令后，会在settings配置的locale目录下生成`.po`文件，每个`.po`文件首先包含一小部分元数据，例如翻译维护者的联系信息，但文件的大部分是翻译对照：被翻译字符串和特定语言的实际翻译文本之间的简单映射。

        ```po
        # SOME DESCRIPTIVE TITLE.
        # Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
        # This file is distributed under the same license as the PACKAGE package.
        # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
        #
        #, fuzzy
        msgid ""
        msgstr ""
        "Project-Id-Version: PACKAGE VERSION\n"
        "Report-Msgid-Bugs-To: \n"
        "POT-Creation-Date: 2019-07-24 15:26+0800\n"
        "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
        "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
        "Language-Team: LANGUAGE <LL@li.org>\n"
        "Language: \n"
        "MIME-Version: 1.0\n"
        "Content-Type: text/plain; charset=UTF-8\n"
        "Content-Transfer-Encoding: 8bit\n"
        "Plural-Forms: nplurals=1; plural=0;\n"
        
        #: .\templates\test_language\test.html:11
        msgid "xxxxxxxxxx"
        msgstr "这些就是xxxx"
        
        #: .\templates\test_language\test.html:12
        #, python-format
        msgid "This string will have %(value)s inside. "
        msgstr "xxxxxxxxxxxxx %(value)s xxxxxxxxxxxxx"
        
        #: .\test_language\views.py:8
        msgid "Welcome to my site!"
        msgstr "欢迎来到我的站点！"
        ```

        - 需要关注的是这样的条目

        ```po
        #: .\test_language\views.py:8
        msgid "Welcome to my site!"
        msgstr "欢迎来到我的站点！"
        ```

        - 这三行内容各自代表下面的意思：
            - 第一行通过注释表达该条要翻译的字符串在视图或模版中的位置；
            - msgid：要翻译的字符串。不要修改它。
            - msgstr：翻译后的文本。一开始它是空的，需要翻译人员逐条填写。

    - 完成上述步骤后，执行`python manage.py compilemessages`对`.po`文件进行编译成对应的`.mo`文件

        - Django在运行时将使用`*.mo`文件对网站进行国际化翻译。

        - 也可以使用`django-admin compilemessages`命令

## 关于.po文件的问题

- 有时候, 用makemessages生成的.po文件中有些msgid会被标记为 fuzzy，比如

    ```powershell
    #: models.py:35
    #, fuzzy
    msgid "hdapp_leader"
    msgstr "领队" 
    ```

    - 这是因为对于 "hdapp_leader",  msgmerge工具认为这个和之前的一个msgid很相似,这个翻译可能不靠谱,于是标记fuzzy； msgfmt就会把这个msgid给略过,也就是这个翻译不会生效,当然如果我们确认是对的, 就手动删掉那行fuzzy,重新compilemessages就好.



## ugettext和ugettext_lazy的区别

Django API 提供了几个有用的模块来帮助你翻译你的应用程序. 它们都在`django.utils.translation`中使用，大多数情况下， 我们会使用到ugettext()和ugettext_lazy().

「u」前缀代表「unicode」, 因为大多数情况下，我们经常使用 Unicode,  所以使用ugettext()代替gettext(), 使用ugettext_lazy()代替gettext_lazy().

顾名思义, lazy该函数是对翻译字符串的引用， 而不是实际翻译的文本. 因此在访问值的时候会进行转换， 而不是调用的时候.

注意这个特性，Django 启动的时候一些特定的代码只执行一次， 比如在**models**, **forms**和**model forms**.

那么， 我们假设在模型定义的时候使用ugettext(), 而不是ugettext_lazy()会怎么样?

- \1. Django 启动, 默认语言是英文.
- \2. Django 选择了英文版的field labels
- \3. 用户将网站语言改为简体中文.
- \4. **field labels**依然是英文显示. 

>   因为models的字段定义仅仅被执行一次，并且在执行定义代码的时候语言不是简体中文(一般是英文).

要避免这种行为，要必须正确的使用ugettext()和ugettext_lazy()

下面总结了， 在合适的地方使用合适的函数:

- ugettext_lazy():
    - models.py (fields, verbose_name, help_text, methods short_description);
    - forms.py (labels, help_text, empty_label);
    - apps.py (verbose_name).
- ugettext():
    - views.py
    - 其他类似于在请求过程中调用的代码