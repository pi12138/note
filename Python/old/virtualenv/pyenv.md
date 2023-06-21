# Pyenv

- Python解释器管理工具
- [参考](<https://zhuanlan.zhihu.com/p/36402791>)

```md
# 查看当前版本
pyenv version

# 查看所有版本
pyenv versions

# 查看所有可安装的版本
pyenv install --list

# 安装指定版本
pyenv install 3.6.5
# 安装新版本后rehash一下
pyenv rehash

# 删除指定版本
pyenv uninstall 3.5.2

# 指定全局版本
pyenv global 3.6.5

# 指定多个全局版本, 3版本优先
pyenv global 3.6.5 2.7.14

# 实际上当你切换版本后, 相应的pip和包仓库都是会自动切换过去的
```

## Pyenv-virtualenv

- 与pyenv 搭配的Python虚拟环境管理工具

  ```md
  # 创建一个3.6.5版本的虚拟环境, 命名为v365env, 然后激活虚拟环境
  $ pyenv virtualenv 3.6.5 v365env
  $ pyenv activate v365env
  # 关闭虚拟环境
  $ pyenv deactivate v365env
  ```

## 注意

- 1.在使用环境的时候**不要用sudo**,否则就变成使用全局环境了（例如安装django,直接pip install django就行了,不要用sudo pip install. ）

## Ubuntu使用pyenv安装2.7时出现的问题

- 如果你在编译旧的python版本（<3.5）时遇到麻烦，即使在ubuntu上安装推荐的软件包之后，更改openssl lib可能有所帮助：

```shell
sudo apt-get remove libssl-dev
sudo apt-get update
sudo apt-get install libssl1.0-dev
```
