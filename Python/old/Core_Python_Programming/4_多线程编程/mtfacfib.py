from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))


def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))


def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))


func = [fib, fac, sum]
n = 12 


def main():
    nfuncs = range(len(func))

    print('*** Single Thread')
    for i in nfuncs:
        print('starting {} at: {}'.format(func[i].__name__, ctime()))
        print(func[i](n))
        print('{} finished at: {}'.format(func[i].__name__, ctime()))

    print('\n *** Multiple Threads')
    threads = []

    for i in nfuncs:
        t = MyThread(func[i], (n,), func[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].get_result())

    print('All Done')


if __name__ == "__main__":
    main()