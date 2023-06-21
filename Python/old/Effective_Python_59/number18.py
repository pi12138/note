def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print("{}: {}".format(message, values_str))


log('My number are', [1, 2])
log("Hi there", [])
