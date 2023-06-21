# coding:utf-8
"""用户登录验证"""
import pymysql


def connect_mysql(id, password):
    db = pymysql.connect('localhost', 'root', 'root', 'python3')
    cursor1 = db.cursor()

    # 查询所有的id，然后将所有id放到一个链表中
    sql1 = "SELECT id FROM userinfo"

    id_list = []

    cursor1.execute(sql1)
    result = cursor1.fetchall()
    # print(result)
    for i in result:
        # print(i)
        # 将id全部添加到id_list中
        id_list.append(i[0])

    # print(id_list)

    # 登录验证部分
    if id not in id_list:
        print('id不存在')
    else:
        # 查询指定id的password
        sql2 = "SELECT password FROM userinfo WHERE id=%s"
        params = [id]

        cursor1.execute(sql2, params)
        # 获得数据库表中的password
        table_pw = cursor1.fetchone()[0]

        if password == table_pw:
            print('登陆成功')
        else:
            print('密码错误')

    cursor1.close()
    db.close()


def input_info():
    """用户输入"""
    id = input("input id:")
    password = input("input password:")
    info = (id, password)

    return info


if __name__ == "__main__":
    info = input_info()
    id, password = info

    connect_mysql(id, password)