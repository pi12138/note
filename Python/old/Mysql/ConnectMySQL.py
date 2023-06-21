# coding:utf-8
"""封装到类
    使用python对数据库进行交互
"""

import pymysql


class ConnectMysql(object):
    """连接mysql数据库类"""
    def __init__(self, host, port, user, password, db):
        """初始化参数"""
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cursor = None

    def connect(self):
        """连接操作"""
        # 连接数据库
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        # 创建光标
        self.cursor = self.conn.cursor()

    def close(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()

    # 可以直接写在需要使用的函数内，不一定要单独定义一个函数
    # def commit(self):
    #     """提交到数据库"""
    #     self.conn.commit()

    def modify_db(self, sql, params=None):
        """需要修改数据库的一些操作，比如增加(insert into)，修改(update)，删除(delete)"""
        try:
            self.connect()
            # 执行sql操作
            count = self.cursor.execute(sql, params)
            # 需要提交到数据库
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count

    def insert(self, sql, params=None):
        """插入数据"""
        return self.modify_db(sql, params)

    def update(self,sql, params=None):
        """更新数据"""
        return self.modify_db(sql, params)

    def delete(self, sql, params=None):
        """删除数据"""
        return self.modify_db(sql, params)

    def select_one(self, sql, params=None):
        """查询一行操作"""
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result       # 返回一个元组

    def select_all(self, sql, params=None):
        """查询多行操作"""
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return result


if __name__ == "__main__":
    """测试代码"""
   
    # 连接数据库
    try:
        # 创建一个连接对象, 同时初始化参数，host，port，user，password, db
        db = ConnectMysql('localhost', 3306, 'root', 'root', 'python3')
        print("数据库链接成功")
    except Exception as e:
        print("error:{}".format(e))

    # 数据库交互操作
    while(True):      
        try:    
            sql = input("请输入sql语句:")
            
            if sql == r"\q":
                break
            # result1 = db.select_one(sql)
            # print(result1)
            result2 = db.select_all(sql)
            # print(result2)
            for i in result2:
                print(i)
        except Exception as e:
            print('error:{}'.format(e))
    print('bye')