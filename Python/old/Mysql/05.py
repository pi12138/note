# coding:utf-8

"""sql语句参数化"""

import pymysql


def connect_sql():
    db = pymysql.connect(host='localhost', port=3306, db='python3', user='root', password='root')
    cursor1 = db.cursor()
    id = input("input id:")
    name = input("input name:")
    age = input("input age:")
    sex = input("input sex:")
    class_ = input("input class:")
    parameters = [id, name, age, sex, class_]

    sql = "INSERT INTO student_info" \
          "(id, name, age, sex, class)" \
          "VALUES " \
          "(%s, %s, %s, %s, %s)"

    cursor1.execute(sql, parameters)
    # 提交到数据库
    db.commit()

    cursor1.close()
    db.close()


if __name__ == "__main__":
    connect_sql()