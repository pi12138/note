# coding:utf-8

"""操作数据库"""
import pymysql
from hashlib import sha1


class OperationMysql(object):
    """操作数据库"""

    def __init__(self, host, user, password, db, port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        """连接"""
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port)
        self.cursor = self.conn.cursor()

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

    def modify_db(self, sql, params):
        """需要修改数据库的操作"""
        self.connect()

        try:
            count = self.cursor.execute(sql, params)
            # 提交到数据库
            self.conn.commit()
        except Exception as e:
            print("modify_db error:", e)

        self.close()
        return count

    def insert(self, sql, params=[]):
        """插入操作"""
        self.modify_db(sql, params)
        print("insert ok")

    def update(self, sql, params=[]):
        """更新操作"""
        self.modify_db(sql, params)
        print('update ok')

    def delete(self, sql, params=[]):
        """删除操作"""
        self.modify_db(sql, params)
        print('delete ok')

    def create_table(self, sql, params=[]):
        """创建数据表"""
        self.modify_db(sql, params)
        print('create table ok')

    def select(self, sql, params=[]):
        """查找"""
        self.connect()

        try:
            self.cursor.execute(sql, params)
            # 获得所有查找内容
            result = self.cursor.fetchall()
            # print(result)
            # result = result[0][0]
        except Exception as e:
            print("select error", e)

        self.close()
        return result


def create_new_table():
    # 创建一个新表userinfo2, password为CHAR(40)是因为sha1加密后的密码大小为40个字符
    sql = "CREATE TABLE userinfo2" \
          "(id VARCHAR(20) NOT NULL," \
          " password CHAR(40) NOT NULL," \
          "PRIMARY KEY(id))"

    db = OperationMysql('localhost', 'root', 'root', 'python3')

    # table_name = input('input table name:')
    db.create_table(sql)


def insert_sha1_date(id, password_sha1):
    """向创建的userinfo2中插入加密后的数据"""
    sql = "INSERT INTO userinfo2" \
          "(id, password)" \
          "VALUES" \
          "(%s, %s);"

    db = OperationMysql('localhost', 'root', 'root', 'python3')

    db.insert(sql, [id, password_sha1])


def sha1_data():
    """加密输入的password"""
    id = input('input id:')
    password = input("input password:")

    # 加密数据
    s1 = sha1()
    s1.update(password.encode())
    # 返回加密的16进制结果
    password_sha1 = s1.hexdigest()
    print(password_sha1)

    info = (id, password_sha1)
    return info


if __name__ == "__main__":
    # create_new_table()
    id, pw = sha1_data()

    insert_sha1_date(id, pw)

