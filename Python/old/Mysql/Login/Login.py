# coding:utf-8

"""用户登录验证"""

from OperationMysql import OperationMysql
from hashlib import sha1


def input_info():
    """输入id和password并对password进行加密"""
    id = input("input id:")
    password = input("input password:")

    s1 = sha1()
    s1.update(password.encode())
    password_sha1 = s1.hexdigest()

    info = (id, password_sha1)
    return info


def login(id, password_sha1):
    """登录验证"""
    db = OperationMysql('localhost', 'root', 'root', 'python3')
    sql = "SELECT password FROM userinfo2 WHERE id=%s"
    # 返回的应该是一条密码
    result = db.select(sql, [id])

    # 验证步骤
    if len(result) == 0:
        # 如果结果为空，表示该id不存在
        print("该id不存在")
    elif result[0][0] != password_sha1:
        print("密码错误！")
    else:
        print("登陆成功")


if __name__ == "__main__":
    id, pw = input_info()
    login(id, pw)
