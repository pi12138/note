# 部署

- 查看 uwsgi 运行情况`ps ajx|grep uwsgi`
- 启动`uwsgi` `uwsgi --ini uwsgi.ini`（停止使用`uwsgi --stop uwsgi.ini`，注意：为了确保项目可以正常运行，可以先使用 `python manage.py runserver`来确定项目是否存在问题）
- 运行Django收集静态文件的命令 `python manage.py collectstatic`，执行该命令后，静态文件会被收集到`collect_static`文件夹下。