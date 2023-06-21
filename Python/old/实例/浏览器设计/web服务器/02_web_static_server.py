'''
静态文件的web服务器
'''

import socket
from multiprocessing import Process
import re

# HTML_ROOT_DIR = './html/'

def handle(client_socket):
    request_data = client_socket.recv(1024)
    request_data = request_data.decode()
    print("request data:", request_data)
    file_name = re.findall('GET /(.*) HTTP', request_data)[0]
    print(file_name)
    # 文件操作
    file = open("./" + file_name, 'rb')
    content = file.read()
    content = content.decode()
    file.close()

    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server: My server\r\n'
    response_body = content
    response = response_start_line + response_headers + '\r\n' + response_body

    client_socket.send(bytes(response, 'utf-8'))

    client_socket.close()

if __name__ == "__main__":
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    post = 9999
    address = (host, post)
    ss.bind(address)
    ss.listen(128)

    while True:
        client_socket, client_address = ss.accept()
        print("客户端地址：", client_address)
        
        client_socket_process = Process(target=handle, args=(client_socket,))
        client_socket_process.start()
        
        client_socket.close()