from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        averager = total/count

    return Result(count, averager)