# 视图

## 查看当前数据库有多少个视图

- show tables; 可以查看所有表，包含基本表(table_type="BASE TABLE")和视图(table_type="VIEW")
- ```mysql
	 select table_name from information_schema.tables where table_schema="blog" and table_type="VIEW"; 
  ```

## 创建视图

```mysql
CREATE VIEW 视图名 AS SELECT 查询语句;
```

## 删除视图

```mysql
DROP VIEW 视图名;
```


