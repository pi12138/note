#!/bin/bash

# 检查参数数量
if [ $# -ne 2 ]; then
    echo "Usage: $0 <command> <num_runs>"
    exit 1
fi

# 获取命令和运行次数
command=$1
num_runs=$2

# 使用 for 循环运行命令指定次数
for ((i=1; i<=num_runs; i++))
do
    echo "Running iteration $i"
    eval $command
done