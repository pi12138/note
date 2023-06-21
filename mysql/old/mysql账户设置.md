# mysql账户管理

## mysql 用户设置

- mysql中**用户注册表**保存在 **mysql数据库的user表中**，如果你需要添加Mysql用户，你只需在该表中添加数据

- 示例

  ```mysql
  INSERT INTO user(host,user,password,select_priv, insert_priv,update_priv,delete_priv,create_priv,drop_priv,ssl_cipher,x509_issuer,x509_subject)
  VALUE('localhost','admin',PASSWORD('admin'),'Y','Y','Y','Y','Y','Y',0,0,0);	
  ```

- 上面代码在创建新用户admin的同时也为该用户赋予了几项权限

- 创建新用户时 密码需要用**PASSWORD() **函数加密

- 创建新用户后，要在命令行输入 "flush privileges；"命令，刷新系统权限表（不然退出root账户后依然无法登录新用户，flush 刷新  privileges 特权）

- 参考[W3Cschool](https://www.w3cschool.cn/mysql/mysql-administration.html)

- 查看当前用户："mysql> select user();"

