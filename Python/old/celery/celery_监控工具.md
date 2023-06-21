# celery监控工具

## flower

- 一个由tornado编写的工具
- 安装：`pip install flower`
- 启动：`celery flower --address=0.0.0.0 --port 5555 --broker=xxx --basic_auth=username:password`
- 在django中启动：`python manage.py celery flower`

## supervisor

- 进程管理工具
- 安装：`pip install supervisor`
- start: `supervisord -c /etc/supervisord.conf`
- reload: `supervisorctl -c supervisord.conf reload`
- stop: `supervisorctl -c supervisord.conf shutdown`
- Tool：supervisorctl

- 配置文件重定向：`echo_supervisord_conf > conf/supervisord.conf`

