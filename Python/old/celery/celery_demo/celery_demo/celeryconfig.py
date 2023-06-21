import djcelery
import datetime

djcelery.setup_loader()

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue',
    }
}

CELERY_IMPORTS = [
    'course.tasks',
]

# 设置默认队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True
# 设置并发的worker数量
CELERYD_CONCURRENCY = 4
# 允许重试
CELERY_ACKS_LATE = True
# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100
# 单个任务的最大运行ii时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': "course-task",
        'schedule': datetime.timedelta(seconds=5),
        'options': {
            'queue': 'beat_tasks',
        } 
    }
}