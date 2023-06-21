# coding:utf-8

import pymysql


def connect_sql():
    db = pymysql.connect(host='localhost', port=3306, db='python3', user='root', password='root')

    cursor1 = db.cursor()

    # 查询mysql版本
    sql = "INSERT INTO student_info" \
          "(id, name, sex, age, class)" \
          "VALUES " \
          "(1615925248, '孔奥辉', '男', 23, '16软件设计二班')"

    cursor1.execute(sql)
    # 插入操作后要执行commit()，不然执行后数据并未插入数据库
    db.commit()

    data1 = cursor1.fetchone()
    print(data1)

    cursor1.close()
    db.close()


if __name__ == "__main__":
    connect_sql()