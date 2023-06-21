class MacroCommend:
    """一个执行一组命令的命令"""
    def __init__(self, commends):
        self.commends = list(commends)

    def __call__(self):
        for commend in self.commends:
            commend()


def func1():
    print("this is func1")

def func2():
    print('this is func2')


comm_list = [func1 ,func2]


if __name__ == "__main__":
    mc = MacroCommend(comm_list)
    mc()