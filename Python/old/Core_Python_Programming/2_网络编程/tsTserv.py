from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
tcp_ser_sock.bind(ADDR)
tcp_ser_sock.listen(5)

while True:
    print("waiting for connection....")
    tcp_cli_sock, addr = tcp_ser_sock.accept()
    print("...connected from: {}".format(addr))

    while True:
        data = tcp_cli_sock.recv(BUFSIZ)

        if not data:
            break
        tcp_cli_sock.send('[{}] {}'.format(ctime(), data.decode()).encode('utf-8'))

    tcp_cli_sock.close()
tcp_ser_sock.close()