# git 上传文件到 github

1. 登录自己的 github 并创建一个新的仓库test

2. `git clone 新建仓库的url`，执行后本地会出现一个test文件夹

3. 将项目文件复制到test文件夹中

4. 在test文件夹中执行以下命令

   - **git add .        （注：别忘记后面的.，此操作是把Test文件夹下面的文件都添加进来）**

   - **git commit  -m  "提交信息"  （注：“提交信息”里面换成你需要，如“first commit”）**

   - **git push -u origin master   （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）**

