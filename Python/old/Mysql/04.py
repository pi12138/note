# coding:utf-8
"""创建一个新表，执行一系列操作后删除这个表"""
import pymysql


def connect_sql():
    db = pymysql.connect(host='localhost', port=3306, db='python3', user='root', password='root')
    cursor1 = db.cursor()

    # 下面sql语句是才是关键部分
    # 创建表
    sql1 = "CREATE TABLE test_person_info" \
           "(name VARCHAR(10) NOT NULL," \
           " age INT ," \
           " sex CHAR(10)," \
           " PRIMARY KEY(name))"
    # 添加数据
    sql2 = "INSERT INTO test_person_info" \
           "(name, age, sex)" \
           "VALUES" \
           "('张三', 20, 'man')," \
           "('翠花', 21, 'woman')," \
           "('李四', 22, 'man');"
    # 查询表
    sql3 = "SELECT *" \
           "FROM test_person_info"
    # 修改翠花性别为 "女"
    sql4 = "UPDATE test_person_info SET age=23 WHERE name='翠花'"
    # 查询修改后的表
    sql5 = "SELECT *" \
           "FROM test_person_info"
    # 删除'李四'的记录
    sql6 = "DELETE FROM test_person_info WHERE name='李四'"
    # 查询执行删除操作后的表
    sql7 = "SELECT *" \
           "FROM test_person_info"
    # 删除整个表格
    sql8 = "DROP TABLE test_person_info"
    # 查询当前数据库中所有表格
    sql9 = "SHOW TABLES"
    # 执行sql语句
    cursor1.execute(sql1)
    cursor1.execute(sql2)
    cursor1.execute(sql3)
    for i in cursor1.fetchall():
        print(i)
    cursor1.execute(sql4)
    cursor1.execute(sql5)
    for i in cursor1.fetchall():
        print(i)
    cursor1.execute(sql6)
    cursor1.execute(sql7)
    for i in cursor1.fetchall():
        print(i)
    cursor1.execute(sql8)
    cursor1.execute(sql9)
    for i in cursor1.fetchall():
        print(i)

    # 提交操作到数据库
    db.commit()
    cursor1.close()
    db.close()


if __name__ == "__main__":
    connect_sql()