from functools import wraps


def coroutine(func):
    """预激 func"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total += term
        count += 1
        averager = total/count