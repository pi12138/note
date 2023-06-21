# mysql数据导入和导出

## 数据表中数据的导入和导出

- MySQL 中你可以使用 SELECT...INTO OUTFILE 语句来简单的导出数据到文本文件上。
  - `select * from myblog_article into outfile 'filename';`
  - 注意：导出的文件在你的相应数据库的文件夹内。
- MySQL 中提供了LOAD DATA INFILE语句来插入数据。
  -  load data local infile 'blog.txt' into table myblog_article;
  - 如果指定LOCAL关键词，则表明从客户主机上按路径读取文件。如果没有指定，则文件在服务器上按路径读取文件。
- 导出SQL格式的数据
  - `mysqldump -u root -p blog myblog_article > blog.txt`
  - `mysqldump -u root -p 数据库名 数据表名 > 要导出的文件名`

## 完整数据库的导入和导出

### 导出

- `mysqldump -u root -p  database_name>file_anme`
- `mysqldump -u root -p 数据库名>要导出到的文件名`

## 导入

1. 先创建一个新的数据库

2. `use new_database`

3. `source 数据文件路径`

    