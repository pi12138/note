# git常见问题汇总

## Linux下git命令中文显示乱码

- 在bash中输入`git config --global core.quotepath false`
- core.quotepath 设置为false的话,就不会对0x80以上的字符进行quote.中文显示正常
