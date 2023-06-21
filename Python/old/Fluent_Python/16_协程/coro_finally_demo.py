class DemoExecption(Exception):
    """自定义异常"""


def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoExecption:
                print("*** DemoExecption handled. Continuing...")
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')