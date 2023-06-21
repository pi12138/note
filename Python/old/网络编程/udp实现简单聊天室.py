"""
聊天室简单功能：
    - 接收信息
    - 发送信息
需要使用到多线程 threading 模块
使用到socket
"""

import threading
import socket


ip = ""
port = 0
s = None

def main():

    global ip
    global port
    global s

    ip = input("请输入要连接的地址IP:")
    port = int(input("请输入要连接的程序Port:"))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 6667))

    tr = threading.Thread(target=RecvData)
    ts = threading.Thread(target=SendData)

    ts.start()
    tr.start()
    ts.join()
    tr.join()

    s.close()
    print("退出主线程")


def SendData():
    """发送消息"""
    while True:
        data = input("<<")
        s.sendto(data.encode(), (ip, port))


def RecvData():
    """接收消息"""
    while True:
        recvinfo = s.recvfrom(1024)
        print("\n>>接收来自{}的消息：{}\n".format(recvinfo[1], recvinfo[0].decode()))


if __name__ == "__main__":
        
    main()