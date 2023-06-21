# coding:utf-8

import pymysql


def connect_sql():
    db = pymysql.connect(host='localhost', port=3306, db='python3', user='root', password='root')

    cursor1 = db.cursor()

    # 查询mysql版本
    sql = "SELECT VERSION()"

    cursor1.execute(sql)
    # 获取查询结果集的第一个行数据，返回一个元组,！！！fetchone()只能返回第一行数据
    data = cursor1.fetchone()
    print("type(data):", type(data))
    print("version:", data[0])

    db.close()


if __name__ == "__main__":
    connect_sql()