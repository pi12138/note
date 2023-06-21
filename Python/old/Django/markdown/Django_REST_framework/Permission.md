# `Permisssions`权限

- 问题
  - 如何根据登录用户的权限不同，来进行不同视图的访问

- 解决方法：
  - 在执行业务流程前对用户权限进行判断，不同的用户执行的业务流程是不一样的

## 自定义权限使用

- 创建一个权限类，继承BasePermission类，实现类中的has_permission()的方法
- 全局设置在settings文件中，"DEFAULT_PERMISSION_CLASSES"
- 局部设置需要给相应的视图类添加permission_classes字段
- 返回值：
  - True，有权访问
  - False，无权访问

