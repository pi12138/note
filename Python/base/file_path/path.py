"""
文件路径拼接
"""

import os

def main():
    path1 = os.path.join("/home", "user", "downloads//", "www.txt")
    normpath1 = os.path.normpath(path1)

    # 如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
    path2 = os.path.join("/home", "user", "downloads", "/www.txt")
    normpath2 = os.path.normpath(path2)

    print(path1)        # > /home/user/downloads//www.txt
    print(normpath1)    # > /home/user/downloads/www.txt
    print(path2)        # > /www.txt
    print(normpath2)    # > /www.txt

if __name__ == "__main__":
    main()

