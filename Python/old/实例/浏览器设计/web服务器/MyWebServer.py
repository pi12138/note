
'''改写04代码，使用简单框架'''

import socket
import re
import sys

from multiprocessing import Process
# from MyWebFrameWork import Application

HTML_ROOT_DIR = './html'
WSGI_PYTHON_DIR = './WSGIPython'


class HttpServer(object):
    # 封装到类
    # pass
    # 初始化
    def __init__(self, app):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.file_name = 0
        self.app = app
        self.response_start_line = ''
        self.response_headers = ''

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

    def start_response(self, status, headers):
        self.response_start_line = "HTTP/1.1 " + status + '\r\n'

        for header in headers:
            self.response_headers = "{0}: {1}\r\n".format(header[0], header[1])

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        request_data = request_data.decode()

        file_name = re.match('\w+ +(/[^ ]*)+ HTTP', request_data).group(1)
        self.file_name = file_name
        print('file name:', file_name)
        method = re.match('(GET|POST|PUT|DELETE|OPTION|HEAD)+ ', request_data).group(1)

        env = {
            'FILE_NAME': file_name,
            'METHOD': method
        }

        response_body = self.app(env, self.start_response)

        response = self.response_start_line + self.response_headers + '\r\n' + response_body

        client_socket.send(bytes(response, 'utf-8'))

        client_socket.close()


def main():
    # 添加查找目录
    sys.path.insert(1, 'F:\\python\\浏览器设计\\web服务器\\WSGIPython')
    # print(sys.path)
    # 获取参数信息
    list_info = sys.argv[1].split(':')
    file_name, app_name = list_info
    m = __import__(file_name)
    app = getattr(m, app_name)

    http_server = HttpServer(app)
    # 指定ip地址和端口号
    ip = '127.0.0.1'
    port = 9999
    http_server.bind(ip, port)
    http_server.start()


if __name__ == "__main__":
    main()