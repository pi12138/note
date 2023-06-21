from celery.schedules import crontab 
import datetime


BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'


# 导入指定任务模块
CELERY_IMPORTS = [
	'celery_app.task1',
	'celery_app.task2'
]

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