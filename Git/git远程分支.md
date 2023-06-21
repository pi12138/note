# git 远程分支

- 查看远程分支 `git branch -r`
- 拉取远程分支代码到本地    
    - `git checkout -b local_new_branch origin/remote_branch`
    - 如果不成功，执行
    - `git fetch`
    - `git checkout -b local_new_branch origin/remote_branch`
