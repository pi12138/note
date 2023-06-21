# git 删除操作

## `git rm filename`

- 删除工作区及暂存区中的该文件，相当于删除文件后执行`git add`
- `git rm --cached filename`
  - 在不小心将不需要追踪的文件添加到暂存区，想删除暂存区的文件但是不想删除工作区的文件时很有用
- `git rm -f filename`
  - 当工作区或者暂存区文件修改了，防止把修改误删了
- `glob模式`
  - 星号(*) 匹配多个或者0个字符
  - [abc]匹配任意一个列在方括号中的字符
  - 问号(?)只匹配一个任意字符
  - [0-9]、[a-z]匹配范围

## `git mv oldname newname`

- 重命名文件

- 相当于
  1. `mv oldname newname`
  2. `git rm oldname`
  3. `git add newname`