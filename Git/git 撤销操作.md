# git 撤销操作

## git commit -amend

- 撤销上次提交，并将暂存区文件重新提交

## git checkout -- filename

- 拉取暂存区的文件，并将其替换工作区的文件
- 注意与`git checkout branchname`的区别

## git reset HEAD -- filename

- 拉取最近一次提交的版本库种的这个文件到暂存区，该操作不影响工作区

## `git reset --option 版本号`

- --hard
- --mixed
- --soft

## 撤销已提交的文件

- git rm --cache filename
    - 撤销后本地磁盘依旧保留

- git rm filename
    - 撤销后本地磁盘也删除
