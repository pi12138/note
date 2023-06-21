# mysql第一次使用配置

- 正常情况下，mysql安装后，启动服务(/etc/init.d/mysql start)后便可以进行登录
- 但是由于第一次登录没有密码，会导致很多问题。

## 第一次登录设置密码

- 正常情况下登录mysql `mysql -u root -p`，但是由于没有密码，这种方式登录不上
- 为了可以登录进去，使用`sudo mysql -u root -p`, 通过linux的root用户进入mysql

- 我们要清楚，mysql的用户信息都保存在 mysql数据库中的user表中
- 所以

1. 选择数据库 `use mysql;`
2. 查询root用户信息 `select * from user where user="root" \G;`

- 可以查询出root用户
- 然后更改root用户密码

1. `update user set password=PASSWORD("new_password") where user="root";`
2. 刷新权限 flush privileges;
3. 重启mysql `service mysql restart`

- 按照上述步骤执行操作后root用户还是无法登录
- 为了可以登录，新创建一个新的超级用户
- `grant all privileges on *.* to 'new_user'@'localhost' identified by 'new_password' with grant option;`
- 然后刷新权限，重启，即可使用新账户登录mysql


