# git 远程仓库

## 生成ssh密钥

- `ssh-keygen`
- `ssh-keygen -t rsa -C "your_email@example.com"`
- 根据生成密钥的提示，复制生成文件里的密钥
- 在githhub --> settings -->SSH and GPG keys中设置

## `git push`

- `git push [remote-name] [branch-name]`
	- 推送本地代码到远程仓库

## `git pull`

- `git pull github使用仓库网址 branch_name`
- 本地用户下载仓库文件

## `git clone`

- `git clone github使用仓库网址 branch_name`
- 其他用户克隆仓库文件

## 添加远程仓库

- `git remote add <shortname> <url>`
	- shortname 为你添加的远程仓库指定一个引用名称
- `git fetch [remote-name]`
	- 从远程仓库拉取代码，但是不会自动和本地代码合并
	- 和git pull的区别在于，git pull会自动合并本地与拉取下来的代码

## 查看远程仓库

- `git remote`

## 删除远程仓库

- `git remote rm local_remote_name`
    - 移除本地的远程仓库引用

## github上的仓库

- 创建github账号
- 创建仓库
- clone 仓库到本地
- 本地 push到仓库
- pull 代码到本地
- ignoring files
  - 可以忽略一些不想被追踪的文件
- fork and pull request

