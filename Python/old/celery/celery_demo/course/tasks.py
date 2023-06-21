from celery.task import Task
import time


class CourseTask(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start run....')
        time.sleep(4)
        print("end run....")