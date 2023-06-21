import _thread
from time import sleep, ctime
from onethr import loop0, loop1


def main():
    print("starting at: ", ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(5)
    print('all Done at: ', ctime())


if __name__ == "__main__":
    main()