# coding:utf-8

import pymysql


def connect_sql():
    db = pymysql.connect(host='localhost', port=3306, db='python3', user='root', password='root')

    cursor1 = db.cursor()

    # 查询mysql版本
    sql = "SELECT *" \
          "FROM student_info"

    cursor1.execute(sql)
    # 获取查询结果集的第一个行数据，返回一个元组,！！！fetchone()只能返回第一行数据
    # data1 = cursor1.fetchone()
    # 获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
    data2 = cursor1.fetchall()
    # print("type(data):", type(data))
    # print("info", data1)
    # print("infos", data2)
    for i in data2:
        print(i)

    db.close()


if __name__ == "__main__":
    connect_sql()