import socket

def tcp_client():

    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 8888
    addr = (host, port)

    sc.connect(addr)
    while True:
        text = input("输入要发送的内容：")
        if len(text) == 0:
            break
        data = text.encode()

        sc.send(data)

        accept_data = sc.recv(1024)
        accept_text = accept_data.decode()

        print("反馈信息：", accept_text)

    sc.close()


if __name__ == '__main__':
    tcp_client()