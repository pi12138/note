# coding:utf-8
"""
测试编写的ConnectMysql类有没有问题
    测试结果：基本没有问题
"""

from ConnectMySQL import ConnectMysql


def no_params():
    sql1 = "INSERT INTO student_info" \
          "(id, name, sex, age, class)" \
          "VALUES" \
          "(1615925246, '高战阳', '男', '24', '16软件设计二班')"
    sql2 = "DELETE FROM student_info WHERE name='高战阳'"
    sql3 = "UPDATE student_info SET age='16' WHERE name='高战阳'"
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'root'
    db_name = 'python3'
    db_conn = ConnectMysql(host, port, user, password, db_name)

    print(db_conn.insert(sql1))
    # print(db_conn.delete(sql2))
    print(db_conn.update(sql3))

def have_params():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'root'
    db_name = 'python3'

    db_conn = ConnectMysql(host, port, user, password, db_name)

    id = input("input id:")
    name = input("input name:")
    sex = input("input sex:")
    age = input("input age:")
    class_ = input("input class:")
    params1 = [id, name, sex, age, class_]
    params2 = [name]

    sql1 = "INSERT INTO student_info" \
           "(id, name, sex, age, class)" \
           "VALUES" \
           "(%s, %s, %s, %s, %s)"
    sql2 = "DELETE FROM student_info WHERE name=%s"
    sql3 = "UPDATE student_info SET age='16' WHERE name=%s"

    print(db_conn.insert(sql1, params1))
    # print(db_conn.delete(sql2, params2))
    print(db_conn.update(sql3, params2))


if __name__ == "__main__":
    # no_params()
    have_params()

