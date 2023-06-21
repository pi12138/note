from socket import *


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udp_cli_sock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("> ")
    if not data:
        break
    udp_cli_sock.sendto(data.encode(), ADDR)
    data, ADDR = udp_cli_sock.recvfrom(BUFSIZ)
    
    if not data:
        break
    print(data.decode())

udp_cli_sock.close()