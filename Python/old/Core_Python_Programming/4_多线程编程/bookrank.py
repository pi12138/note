from atexit import register
from re import compile
from threading import Thread
from time import ctime
import urllib3


REGEX = compile(r'#([\d,]+) in Books')
AMAZON = 'https://www.amazon.com/gp/product/'
ISBN_10 = {
    '0132269937': 'Core Python Programming (2nd Edition)',
    '0132678209': 'Core Python Applications Programming (3rd Edition)',
    '1491946008': 'Fluent Python: Clear, Concise, and Effective Programming',
}


def get_ranking(isbn):
    url = '{}{}'.format(AMAZON, isbn)
    http = urllib3.PoolManager()
    res = http.request('GET', url)
    data = res.data.decode()
    
    return REGEX.findall(data)[0]


def show_ranking(isbn):
    print('{} ranked {}'.format(ISBN_10[isbn], get_ranking(isbn)))


def main():
    print('at {} on Amazon...'.format(ctime()))
    for isbn in ISBN_10:
        show_ranking(isbn)


@register
def _atexit():
    print('all done at {}'.format(ctime()))


if __name__ == "__main__":
    main()