from bookrank import *
from threading import Thread


def main():
    print('at {} on Amazon...'.format(ctime()))
    for isbn in ISBN_10:
        Thread(target=show_ranking, args=(isbn, )).start()


if __name__ == "__main__":
    main()