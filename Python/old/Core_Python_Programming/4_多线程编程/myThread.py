import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def get_result(self):
        return self.res

    def run(self):
        print('starting {} at: {}'.format(self.name, ctime()))
        self.res = self.func(*self.args)
        print('{} finished at: {}'.format(self.name, ctime()))