from concurrent.futures.thread import ThreadPoolExecutor
from bookrank import *

def main():
    print('At {} on Amazon...'.format(ctime()))

    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBN_10, executor.map(get_ranking, ISBN_10)):
            print('- {} ranked {}'.format(ISBN_10[isbn], ranking))

    # print('all done at: {}'.format(ctime()))


if __name__ == "__main__":
    main()