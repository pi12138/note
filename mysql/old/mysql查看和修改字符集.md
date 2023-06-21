# `MySQL`查看和修改字符集

## 查看字符集

```mysql
mysql> show variables like 'collation_%';
+----------------------+-----------------+
| Variable_name        | Value           |
+----------------------+-----------------+
| collation_connection | gbk_chinese_ci  |
| collation_database   | utf8_general_ci |
| collation_server     | utf8_general_ci |
+----------------------+-----------------+
3 rows in set (0.01 sec)

mysql> show variables like 'character_set_%';
+--------------------------+---------------------------------------------------------+
| Variable_name            | Value                                                   |
+--------------------------+---------------------------------------------------------+
| character_set_client     | gbk                                                     |
| character_set_connection | gbk                                                     |
| character_set_database   | utf8                                                    |
| character_set_filesystem | binary                                                  |
| character_set_results    | gbk                                                     |
| character_set_server     | utf8                                                    |
| character_set_system     | utf8                                                    |
| character_sets_dir       | C:\Program Files\MySQL\MySQL Server 5.6\share\charsets\ |
+--------------------------+---------------------------------------------------------+
8 rows in set (0.01 sec)
```

## 修改字符集

- 切换到需要修改字符集的数据库，use mydb
- 执行，`alter database mydb character set utf8`
- 创建数据库时指定数据库的字符集
  - `create database mydb character set utf8`