# 新建数据表

- 语法
  ```mysql
  CREATE TABLE table_name (column_name column_type);
  ```

- 例如

  ```mysql
  CREATE TABLE IF NOT EXISTS `runoob_tbl`(
     `runoob_id` INT UNSIGNED AUTO_INCREMENT,
     `runoob_title` VARCHAR(100) NOT NULL,
     `runoob_author` VARCHAR(40) NOT NULL,
     `submission_date` DATE,
     PRIMARY KEY ( `runoob_id` )
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;
  ```

  