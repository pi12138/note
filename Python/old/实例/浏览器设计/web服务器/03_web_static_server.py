'''处理new_02中的代码，使用面向对象'''

import socket
import re

from multiprocessing import Process

HTML_ROOT_DIR = './html'


# 封装到类
class HttpServer(object):
    # pass
    # 初始化
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定ip地址和端口号
    def bind(self, ip, port):
        # self.ip = ip
        # self.port = port
        self.ss.bind((ip, port))

    def start(self):
        # pass
        self.ss.listen(128)

        while True:
            client_socket, client_address = self.ss.accept()
            print("客户端地址：", client_address)
            # 多进程
            client_socket_process = Process(target=self.handle_client, args=(client_socket,))
            client_socket_process.start()

            client_socket.close()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        request_data = request_data.decode()

        file_name = re.match('\w+ +(/.*)+ HTTP', request_data).group(1)
        print('file name:', file_name)
        if '/' == file_name:
            file_name = '/index.html'

        try:
            file = open(HTML_ROOT_DIR + file_name, 'rb')
        except Exception:
            response_strat_line = 'HTTP/1.1 404 Not Found\r\n'
            response_headers = 'Server: My Server\r\n'
            response_body = 'This File Not Found'
        else:
            content = file.read()
            content = content.decode()
            file.close()

            response_strat_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My Server\r\n"
            response_body = content

        response = response_strat_line + response_headers + '\r\n' + response_body

        client_socket.send(bytes(response, 'utf-8'))

        client_socket.close()




def main():
    # 创建一个对象
    http_server = HttpServer()
    # 指定ip地址和端口号
    http_server.bind('127.0.0.1', 9999)
    # 启动
    http_server.start()

if __name__ == "__main__":
    main()