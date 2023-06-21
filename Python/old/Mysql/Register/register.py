# coding:utf-8

"""用户注册操作"""

from Register.OperationMysql import OperationMysql
from Register.OperationMysql import sha1


def input_info():
    """输入id和password并对password进行加密"""
    id = input("input id:")
    password = input("input password:")

    s1 = sha1()
    s1.update(password.encode())
    password_sha1 = s1.hexdigest()

    info = (id, password_sha1)
    return info


def register(id, password_sha1):
    """注册验证"""
    db = OperationMysql('localhost', 'root', 'root', 'python3')
    sql = "SELECT password FROM userinfo2 WHERE id=%s"

    result = db.select(sql, [id])
    # print("result:", result)
    if len(result) == 0:
        # 如果result = 0 表示该id数据库里没有，可以注册
        try:
            sql2 = "INSERT INTO userinfo2" \
                   "(id, password)" \
                   "VALUES" \
                   "(%s, %s)"
            db.insert(sql2, [id, password_sha1])
            print("注册成功")
        except Exception as e:
            print("注册失败")
            print("register error:", e)

    else:
        print("该id存在，请重新输入id。")


if __name__ == "__main__":
    id, pw = input_info()
    register(id, pw)
