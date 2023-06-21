# django_使用celery发送邮件

## 需要模块

`pip install celery`
`pip install eventlet`
`pip install django-redis`

## celery简单原理

- 任务发出者将任务发送到 任务队列(中间人, broker)中
- 任务处理者(worker)监听任务队列，并从任务队列中取出任务

- 任务的发出者，中间人，任务处理者可以在同一台机器上启动，也可以不在同一台机器上
- 一般 项目代码 为 任务的发出者
- 可以使用 redis数据库 作为 任务队列
- 任务的处理者 也需要有项目代码

## 基本流程

- 在项目目录下创建 celery_tasks 包
- 在包内编写文件 tasks.py
```python
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
import time

# 任务处理者一端需要有django环境
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
django.setup()


# 创建一个Celery类对象实例
app = Celery('celery_tasks.tasks', broker='redis://:root@127.0.0.1:6379/8')


@app.task
def send_register_email(username, email, token):
    """
    发送激活邮件
    :return:
    """
    subject = '注册激活'
    msg = ''
    from_email = settings.EMAIL_FROM
    to_email = email
    html_msg = "<h2>{}，你好</h2><p>点击下面链接激活你的账户</p><br><a href='http://127.0.0.1:8000/user/active/{}'>http://127.0.0.1/user/active/{}</a>".format(username, token, token)

    send_mail(subject, msg, from_email, [to_email], html_message=html_msg, fail_silently=False)

    time.sleep(3)

```

- 进入相对应的虚拟环境和任务文件所在的文件夹
- 输入 `celery -A celery_tasks.tasks worker -l info -P eventlet`
- (celery -A <mymodule> worker -l info -P eventlet)
- 在views.py内调用自己编写的发送邮件的函数`send_register_email()`
```python
# 4. 发送激活邮件
serializer = Serializer(settings.SECRET_KEY, 3600)
info = {'confirm': user.id}
token = serializer.dumps(info)
token = token.decode()

send_register_email.delay(user_name, email, token)
```

- 当进行请求时即可异步发送邮件