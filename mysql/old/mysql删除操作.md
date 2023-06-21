# mysql 删除操作

##  删除数据表

- 删除单个表
  
- drop table table_name;
  
- 删除多个表

  - drop table a, b, c;

- 无视外键关联删除表

  - ```mysql
    SET foreign_key_checks = 0;
    DROP TABLE IF EXISTS a,b,c;
    SET foreign_key_checks = 1;
    ```



## 删除数据

- 删除一行指定数据
  
  - delete from table_name where table_head = 'info';
  
- 删除一个表中所有数据
  - 清除全部数据，不写日志，不可恢复，速度极快
    - truncate table table_name
  - 清除全部数据，写日志，数据可以恢复，速度慢
    - delete from table_name
  
- 删除一行中的某个列的数据

  - 将该列的数据设置为NULL

  - ```mysql
    update table_name
    set column_name = NULL
    where id = "xxx"
    ```

    

## 删除数据库

## drop 命令删除数据库

- drop 命令格式：
  - drop database <数据库名>;

