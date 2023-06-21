# git 分支

## git分支的创建、修改、切换、删除

- `git branch`
  - 查看分支, 查看本地分支
  - `git branch -r`，查看远程分支
  - `git branch -a`，查看本地分支和远程分支
- `git branch branch_name`
  - 创建分支
- `git branch -m oldname newname`
  - 修改分支名称
- `git checkout branch_name`
  - 切换分支
  - `git checkout -b branch_name`创建分支后，自动切换到刚创建的分支
- `git branch -d branch_name`
  - 删除分支
  - `git push origin  --delete 远程分支名`，删除远程分支
  - `git push origin  -d 远程分支名`
- `git branch local_new_branch remote_name/branch`
  - 基于远程仓库新建一个本地分支

## git新建分支然后推送到远程

- `git push origin 本地分支名`
  - 推送本地分支到远程，远程分支和本地分支同名
  - `git push origin 本地分支名:远程分支名`

## git新建分支和远程进行关联

- `git branch --set-upstream-to=origin/remote_branch local_branch`

## git 分支的合并

### 分支的指针

- HEAD指针指向当前工作分支，在切换分支时指向新的分支

###`git diff`

- `git diff`
  - 比较工作区与暂存区文件的差异
- `git diff --staged`
  - 比较暂存区和版本库的文件差异
- `git diff 版本号 版本号`
  - 比较分支内的两个版本的差异
- `git diff 分支 分支`
  - 比较两个分支最新提交版本的差异

### git merage [branch-name]

- 合并指定分支到当前分支 
- `git merge --abort` 撤销当前合并状态

## 储存变更

- `git stash`
  - 暂时存储当前工作区的文件的修改内容
- `git stash list`
  - 查看当前本地有哪些暂时存储的文件信息
- `git stash apply stash@num`
  - 将暂时存储的文件信息，返回到原文件中
  - `git stash apply`后面不加名字则应用最近一次的存储信息
- `git stash pop stash@num`
  - 将暂时存储的文件信息，返回到原文件中，然后删除在`git stash list`中的文件信息记录
- `git stash drop stash@num`
  - 删除`git stash list`中保存的文件信息记录
  - `git stash apply`只是运用存储的信息，并不删除它，drop命令可以删除它
