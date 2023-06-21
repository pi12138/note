# 消费者
def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return 
        print("Consumer {}".format(n))
        r = "200 Ok"

# 生产者
def produce(c):
    c.send(None)
    n  = 0
    while n < 5:
        n = n + 1
        print("Produce {}".format(n))
        r = c.send(n)
        print("Consumer return {}".format(r))
    c.close()


if __name__ == "__main__":
    c = consumer()
    produce(c)