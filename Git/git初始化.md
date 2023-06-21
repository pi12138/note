# git 初始化

- `git init`

## git链接远程已存在仓库

- `git remote add origin 仓库地址`

- 推送本地代码到远端

  - `git add .`

  - `git commit`

  - `git push --set-upstream origin master`

    

## git链接远程仓库可能出现的问题

- 新建的远程仓库可能和本地的仓库有不同的开始点，直接推送代码可能会有问题

- ` ! [rejected]        master -> master (non-fast-forward)`

- 此时，需要

  - `git pull origin master --allow-unrelated-histories`

  