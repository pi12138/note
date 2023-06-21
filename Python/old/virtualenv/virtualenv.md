# 1.虚拟环境(windows)
	- mkvirtualenv [env_name]	创建虚拟环境
	- rmvirtualenv	[env_name]	删除虚拟环境
	- workon [env_name]			进入虚拟环境
	- deactivate				退出虚拟环境
	
	- 显示已经创建的虚拟环境: workon, lsvirtualenv

# 2.虚拟环境（linux)
- 安装 pip install virtualenv
- 创建虚拟环境
  - virtualenv env_name



# 3.virtualenvwrapper

- **下面操作建议在root权限下进行**
  - su root

　　鉴于virtualenv不便于对虚拟环境集中管理，所以推荐直接使用virtualenvwrapper。 

​	virtualenvwrapper提供了一系列命令使得和虚拟环境工作变得便利。它把你所有的虚拟环境都放在一个地方。

　　安装virtualenvwrapper(确保virtualenv已安装)

```
pip install virtualenvwrapper
pip install virtualenvwrapper-win　　#Windows使用该命令
```

　　安装完成后，在~/.bashrc写入以下内容

```
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh　　
```

　　第一行：virtualenvwrapper存放虚拟环境目录

　　第二行：virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh

```
source ~/.bashrc　　　　#读入配置文件，立即生效
```

# 4.virtualenvwrapper基本使用

1.创建虚拟环境　**mkvirtualenv**

```
mkvirtualenv venv　　　
```

　　这样会在WORKON_HOME变量指定的目录下新建名为venv的虚拟环境。

　　若想指定python版本，可通过"--python"指定python解释器

```
mkvirtualenv --python=/usr/local/python3.5.3/bin/python venv
```

2. 基本命令 　

　　查看当前的虚拟环境目录

```
[root@localhost ~]# workon
py2
py3
```

　　切换到虚拟环境

```
[root@localhost ~]# workon py3
(py3) [root@localhost ~]# 
```

　　退出虚拟环境

```
(py3) [root@localhost ~]# deactivate
[root@localhost ~]# 
```

　　删除虚拟环境

```
rmvirtualenv venv
```
- [参考](https://www.cnblogs.com/technologylife/p/6635631.html)

## win下对virtualenvwrapper进行配置

- win下安装玩virtualenvwrapper后，如果创建虚拟环境，会默认在当前所在目录进行创建，这样很不便于我们进行管理，为了访问我们管理，我们可以添加一些内容到环境变量中
- 变量名：`WORKON_HOME`。
- 变量值：你自己想存放的目录。

## 关于安装后基本命令不能使用的问题

- 将python安装目录下的scripts文件夹添加到环境变量PATH中
- 这个文件夹中有我们经常会使用到的脚本。

## win下py2，py3共存情况下如何创建虚拟环境

- `mkvirtualenv -p D:\python2\python.exe virtualenv_name`

