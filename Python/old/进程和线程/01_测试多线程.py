# 对多线程进行测试，看看任务管理器情况
import time
import threading


def test01():
    print("start test01.....")
    time.sleep(10)
    print("end test01.......")

def test02():
    print("start test02.....")
    time.sleep(20)
    print("end test02.......")


if __name__ == "__main__":
    # test01()
    t1 = threading.Thread(target=test01)
    t2 = threading.Thread(target=test02)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    