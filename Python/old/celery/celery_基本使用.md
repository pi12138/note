# celery

## 安装

- pip install celery[redis]	(使用redis作为消息中间件)

## 消息中间件

- RabbitMQ/Redis

## 基本使用流程

1. 创建一个Celery实例
2. 使用实例装饰一个任务
3. 启动worker

## 启动worker

- `celery worker -A celery_app -l INFO` 
- 参数-A 后面是celery app位置, -l 后面是日志级别

## 定时任务

- 配置文件中编写配置， 将需要定时运行的任务配置到配置文件中
```Python
# 定时任务
CELERYBEAT_SCHEDULE = {
	'task1': {
		'task': 'celery_app.task1.add',
		'schedule': datetime.timedelta(seconds=10),		# 每10s执行一次
		'args': (2, 8)
	},
	'task2': {
		'task': 'celery_app.task2.chengfa',
		'schedule': crontab(hour=16, minute=53),		# 每天16:45执行
		'args': (4, 5)
	}
}
```
- 启动beat `celery beat -A celery_app -l INFO`
- 同时启动worker和beat `celery -B -A celery_app worker -l INFO`
