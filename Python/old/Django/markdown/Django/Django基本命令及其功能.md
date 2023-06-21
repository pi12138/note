# `Django命令`

- `python manage.py help`，查看所有命令

## `models`相关

- `python manage.py check`，验证模型类的有效性，（`python manage.py validate`）
- `python manage.py makemigrations`，生成迁移文件，为数据迁移做准备
- `python manage.py sqlmigrate`，生成迁移文件后，使用该命令可以查看生成表的sql语句
- `python manage.py migrate`，执行迁移文件内容，生成迁移数据到数据库
- `python manage.py syncdb`， 提交sql语句至数据库，Django1.9后被移除