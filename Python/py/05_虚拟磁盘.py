import os
import sys

PATH = "G:\\virtual_disk"

def run_command(cmd):
    """
    运行命令行的命令,返回状态码
    """
    return os.system(cmd)

def run_command_output(cmd):
    """
    运行命令，返回执行结果
    """
    p = os.popen(cmd)

    return p.read()

def run_subst(driver, path):
    """
    创建虚拟磁盘
    先判断虚拟磁盘是否存在，如果存在，则无法创建
    """

    exist = judge_exist(driver)

    if exist:
        return "虚拟磁盘{}已存在！".format(driver)
    else:
        subst = "subst {} {}".format(driver, path)
        code = run_command(subst)

        if code == 0:
            return "创建虚拟磁盘{}成功！".format(driver)

def run_unsubst(driver):
    """
    删除虚拟磁盘
    先判断虚拟磁盘是否存在，如果存在则进行删除操作
    """

    exist = judge_exist(driver)

    if exist:
        unsubst = "subst {} /D".format(driver)
        code = run_command(unsubst)

        if code == 0:
            return "删除虚拟磁盘{}成功！".format(driver)
    else:
        return "该虚拟磁盘不存在！"


def find_all_virtual_disk():
    """
    查找所有虚拟磁盘
    """
    result = run_command_output("subst")
    
    return result

def judge_exist(driver):
    """
    判断虚拟磁盘是否存在
    先将已有的虚拟磁盘盘符放到列表中，然后判断是否存在，若存在返回True，若不存在返回False
    """
    result = find_all_virtual_disk().split('\n')

    driver_list = []
    for i in result[0:-1]:
        driver_list.append(i[0:2])

    if driver in driver_list:
        return True
    else:
        return False

def stop():
    os.system("pause")
    os.system("cls")

def main():
    print("选择操作：")
    print("1. 查看已有虚拟磁盘。")
    print("2. 创建新的虚拟磁盘。")
    print("3. 删除已有虚拟磁盘。")
    print("点击其他按键退出")

    num = input("选择操作：")

    if num == "1":
        disks = find_all_virtual_disk()
        print(disks)
        stop()

    elif num == '2':
        data = input("输入虚拟磁盘盘符：")
        result = run_subst(data, PATH)
        print(result)
        stop()

    elif num == '3':
        data = input("输入要删除的虚拟磁盘盘符：")
        result = run_unsubst(data)
        print(result)
        stop()

    else:
        sys.exit()

if __name__ == "__main__":

    while True:
        main()




