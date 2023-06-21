import inspect


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


def simple_coroutine2(a):
    print('-> Started: a=', a)
    b = yield a
    print('-> Received: b=', b)
    c = yield a + b
    print('-> Received: c=', c)


if __name__ == "__main__":
    # coro = simple_coroutine()
    # print(coro)

    # next(coro)
    # print(inspect.getgeneratorstate(coro))

    # coro.send(42)

    coro2 = simple_coroutine2(14)
    print(inspect.getgeneratorstate(coro2))

    next(coro2)
    print(inspect.getgeneratorstate(coro2))
    print(coro2.send(28))
    coro2.send(99)

    print(inspect.getgeneratorstate(coro2))