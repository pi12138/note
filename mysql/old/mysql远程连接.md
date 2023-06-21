# mysql远程连接

## 关闭远程连接

1. 使用root用户登录到数据库
2. use mysql 选择mysql数据库
3. revoke all privileges on *.* from 'root'@'%'; 撤回权限
4. delete from user where User="root" and Host="%"; 删除用户
5. flush privileges; 刷新

## 开启远程连接

1. 找到mysql的配置文件，注释或者修改掉bind-address
2. 登陆mysql给对应的账户分配权限
    - `GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';`
3. flush privileges; 刷新
4. service mysql restart 重启mysql

## mysql 5.7开启远程连接

1. 找到mysql的配置文件，Ubuntu配置文件地址在`/etc/mysql/mysql.conf.d/mysqld.cnf`
2. 修改配置文件中的bind-address，注释掉或者改成0.0.0.0(默认为127.0.0.1)
3. 登录本地mysql，创建一个新的账户，并且分配权限
    - `GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION`
4. 刷新权限 `flush privileges`
5. 重启mysql `service mysql restart`
6. 关闭linux防火墙
