# mysql的卸载

- 卸载mysql的目的是为了更好的重装
- mysql如果卸载的不干净会导致重装其他版本不行

## 卸载步骤

- `sudo apt purge mysql-*`
- `sudo rm -rf /etc/mysql`
- `sudo rm -rf /var/lib/mysql`
- `sudo apt autoremove`
- `sudo apt autoclean`

- 测试版本为mysql 5.7 

 
