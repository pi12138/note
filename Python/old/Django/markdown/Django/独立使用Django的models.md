# `独立使用Django的model`

```python
# 独立使用Django的models

import os
import sys

# 返回当前文件所在目录
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")

# 每个项目的下面部分稍微有些不同，可以在manage.py文件中找到
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'MXShop.settings')

import django
django.setup()
```

- 可以将这部分代码配置到`settings -> Bulid,Execution,Deployment -> Console -> Python Console`
- 配置完成后保存，然后可以在Python Console中直接使用项目的models文件。

