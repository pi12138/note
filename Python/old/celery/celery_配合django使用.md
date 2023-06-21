# 在django中使用celery

## 安装

- `pip install django-celery`

## 启动worker

- worker： python manage.py celery worker -Q queue
- 如果想要执行上面的命令必须将djcelery加入到setting的INSTALLED_APPS中

## 启动beat

- beat: python manage.py celery beat -l INFO
