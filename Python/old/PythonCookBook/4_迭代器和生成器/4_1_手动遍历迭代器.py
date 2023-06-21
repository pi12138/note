
a = [1, 2, 3, 4, 5]
a = iter(a)


# print(next(a))
def func(it):
    try:
        while True:
            print(next(it))
    except Exception as e:
        print("error: {}".format(e))


def func2(it):
    while True:
        n = next(it, None)
        print(n)

        if n is None:
            break


if __name__ == "__main__":
    # func(a)
    func2(a)