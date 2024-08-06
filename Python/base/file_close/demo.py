import time


def one():
    f = open("/tmp/one.txt", "r")
    print(f.read())
    f.close()
    time.sleep(10 * 60)


def main():
    one()
    time.sleep(10 * 60)

if __name__ == "__main__":
    main()