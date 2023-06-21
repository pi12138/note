"""
简单实现上下文管理器
"""


class Context():
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, type, value, traceback):
        print("exit")


class Transactions():
    """
    数据库事务上下文管理器
    """
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.db.begin()

    def __exit__(self, type, value, traceback):
        if type is None:
            db.commit()
        else:
            db.rollback()


def main():
    with Context():
        print("context")


if __name__ == "__main__":
    main()