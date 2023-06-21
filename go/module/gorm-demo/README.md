# Readme

## 数据库

- `mysql  Ver 8.0.30-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))`
- 创建数据库和创建用户并赋予权限

    ```shell
    create database if not exists gormdemo default character set = "utf8";
    create user "gormdemo"@"localhost" identified by "password";
    grant all on gormdemo.* to "gormdemo"@"localhost";
    FLUSH PRIVILEGES;
    ```

- 开启 mysql 的通用日志

    ```shell
    set global log_output=file;
    set global general_log_file='/var/lib/mysql/VM-16-5-ubuntu.log';
    set global general_log=on;
    ```

### 其他 mysql 相关

- 删除表 `drop table TableName`
- 查看表结构 `desc TableName`
- 查看建表语句 `show create table TableName`
