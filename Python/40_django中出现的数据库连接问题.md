# django连接数据库问题

- django2.2
- python3.6

## django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module

- 解决方案1: 在__init__.py中添加

```python
import pymysql

pymysql.install_as_MySQLdb()
```

- 要先安装pymysql

- 解决方案2: 安装mysqlclient
- 要先安装一些前置包
- `sudo apt-get install python-dev libmysqlclient-dev`
- `sudo apt-get install python3-dev`
