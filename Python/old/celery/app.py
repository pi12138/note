from celery_app.task1 import add
from celery_app.task2 import chengfa


add.delay(2, 8)
chengfa.delay(4, 5)