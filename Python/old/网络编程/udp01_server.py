"""
UDP服务器端
    1.建立socket
    2.绑定ip+port
    3.接收访问(recvfrom())
    4.返回/反馈(sendto())
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print("9999端口已开启....")
while True:
    data, addr = s.recvfrom(1024)
    print("接收到来自{}的信息:{}".format(addr, data.decode()))
    s.sendto("谢谢发送".encode(), addr)