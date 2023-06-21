# git基本命令

## git init

- git init
  - 初始化git仓库
  - 出现 .git 文件

## git add

- git add filename
  - 将文件添加到暂存区
- git add .
  - 将工作目录下的所有修改的文件添加到暂存区

## git commit

- git commit -m 'description'
  - 将暂存区文件提交到版本库
- git commit -am 'description'
  - 跳过 `git add`添加到暂存区命令，直接将工作区所有**已跟踪**的文件提交

## git log

- 查看提交日志

## git status

- 查看项目文件状态

## git config

- git config --global user.name 'username'
- git config --global user.email 'useremail'
- git config --list
- 地址 ~/.gitconfig