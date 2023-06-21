'''
完善02里面的代码
'''

import re
import socket

from multiprocessing import Process

HTML_ROOT_DIR = './html'

def handle_client(client_socket):
    '''处理客户端请求'''
    # 接收请求
    request_data = client_socket.recv(1024)
    request_data = request_data.decode()
    print('request data:\n', request_data)

    # 使用正则表达式提取url
    # GET /html/index.html HTTP/1.1
    file_name = re.match(r'\w+ +(/[^ ]*) HTTP', request_data).group(1)
    print("file name:", file_name)

    if '/' == file_name:
        file_name = '/index.html'

    try:
        # 打开文件
        file = open(HTML_ROOT_DIR + file_name, 'rb')
    except Exception as e:
        print('error:', e)

        # 编写文件不存在时的response
        response_start_line = 'HTTP/1.1 404 Not Found\r\n'
        response_headers = "Server: MY SERVER\r\n"
        response_body = 'Not Found This File'
    else:
        content = file.read()
        content = content.decode()      # response_body数据要求是str
        file.close()

        # 编写response
        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = "Server: MY SERVER\r\n"
        response_body = content

    response = response_start_line + response_headers + '\r\n' + response_body
    # print("response:", response)

    # 发送给浏览器
    client_socket.send(bytes(response, 'utf-8'))
    client_socket.close()


def web_static_server():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ss.bind(('127.0.0.1', 9999))
    ss.listen(128)

    while True:
        client_socket ,client_address = ss.accept()
        print("client address:", client_address)

        client_socket_process = Process(target=handle_client, args=(client_socket, ))
        client_socket_process.start()

        client_socket.close()


if __name__ == "__main__":
    web_static_server()