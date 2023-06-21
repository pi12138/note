'''
固定响应数据
'''

import socket
from multiprocessing import Process
import re

def func(socket_object):
    '''进程处理函数'''
    # 接收请求数据
    request_data = socket_object.recv(1024)
    request_data = request_data.decode()
    print("request data:", request_data)
    find_data = re.findall('Referer: (.*)\r', request_data)
    print("find_data:", find_data)
    # print(type(request_data))
    # request_data = request_data.split('\r\n')
    # print(type(request_data))
    # print("request data", request_data)
    
    # # 构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: my server\r\n'
    response_body = 'Hello, This is my server!'
    response = response_start_line + response_headers + '\r\n' + response_body

    # 发送给服务器响应数据
    socket_object.send(bytes(response, 'utf-8'))
    # 关闭客户端连接
    socket_object.close()

if __name__ == "__main__":
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "127.0.0.1"
    port = 9999

    ss.bind((host, port))
    ss.listen(128)

    while True:
        socket_object, socket_address = ss.accept()
        print("socket address:", socket_address)
        p = Process(target=func, args=(socket_object,))
        p.start()
        socket_object.close()

    ss.close()


    