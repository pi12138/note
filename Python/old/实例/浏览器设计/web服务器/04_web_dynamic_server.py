'''由03代码添加访问动态资源'''

import socket
import re
import sys
import tkinter

from multiprocessing import Process

HTML_ROOT_DIR = './html'
WSGI_PYTHON_DIR = './WSGIPython'


class HttpServer(object):
    # 封装到类
    # pass
    # 初始化
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.file_name = 0

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

        if file_name.endswith('.py'):
            module_name = file_name[1:-3]
            print('module name:', file_name)
            try:
                module_name = __import__(module_name)
            except Exception:
                self.response_start_line = 'HTTP/1.1 404 Not Found\r\n'
                self.response_headers = 'Server: My Server\r\n'
                response_body = 'This File Not Found'

            else:
                # env为客户端传过来的数据解析内容
                env = {
                    'FILE_NAME': file_name,
                    'METHOD': method
                }
                response_body = module_name.application(env, self.start_response)

            response = self.response_start_line + self.response_headers + '\r\n' + response_body

        else:
            if '/' == file_name:
                file_name = '/index.html'

            try:
                file = open(HTML_ROOT_DIR + file_name, 'rb')
            except Exception:
                response_start_line = 'HTTP/1.1 404 Not Found\r\n'
                response_headers = 'Server: My Server\r\n'
                response_body = 'This File Not Found'
            else:
                content = file.read()
                content = content.decode()
                file.close()

                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My Server\r\n"
                response_body = content

            response = response_start_line + response_headers + '\r\n' + response_body

        client_socket.send(bytes(response, 'utf-8'))

        client_socket.close()


def main():
    # 添加查找目录
    sys.path.insert(1, 'F:\\python\\浏览器设计\\web服务器\\WSGIPython')
    # print(sys.path)

    '''编写服务器简单界面'''

    base = tkinter.Tk()
    base.title('Web Server')
    base.geometry('500x500')

    label1 = tkinter.Label(base, text='IP:')
    label1.pack()
    entry1 = tkinter.Entry(base, show=None, bg='gray')
    entry1.pack()

    label2 = tkinter.Label(base, text='Port:')
    label2.pack()
    entry2 = tkinter.Entry(base, show=None, bg='gray')
    entry2.pack()

    var = tkinter.StringVar()

    def start():
        # global ip, port
        ip = entry1.get()
        port = entry2.get()

        var.set("服务器({0},{1})启动".format(ip, port))

        ip = entry1.get()
        port = int(entry2.get())
        print(ip, port)

        http_server = HttpServer()
        # 指定ip地址和端口号
        http_server.bind(ip, port)
        http_server.start()
        # var.set("浏览器请求文件：", http_server.file_name)

    button1 = tkinter.Button(base, text='开启', command=start)
    button1.pack()

    label3 = tkinter.Label(base, textvariable=var, bg='gray', width=50, height=30)
    label3.pack()

    # text1 = tkinter.Text(base, bg='gray', width=50, height=30)
    # text1.pack()

    # 启动


    base.mainloop()

if __name__ == "__main__":
    main()