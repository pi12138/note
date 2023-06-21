from socket import *


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
    tcp_cli_sock.connect(ADDR)
    data = input("> ")

    if not data:
        break
    tcp_cli_sock.send('{}\r\n'.format(data).encode())
    data = tcp_cli_sock.recv(BUFSIZ)

    if not data:
        break

    print(data.decode().strip())
    tcp_cli_sock.close()