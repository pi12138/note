"""
TCP客户端
    1.socket建立
    2.发送消息到指定服务器(ip + port)
    3.等待反馈
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 客户端绑定端口号，如果不绑定则由系统自动分配
s.bind(('127.0.0.1', 6666))

text = '你好'.encode()

s.sendto(text, ('127.0.0.1', 9999))

data, addr = s.recvfrom(1024)

print("接收到来自{}的反馈信息:{}".format(addr, data.decode()))