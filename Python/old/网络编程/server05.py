import socket

def tcp_server():

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 8888
    addr = (host, port)

    ss.bind(addr)
    ss.listen(5)
    while True:
        conn, address = ss.accept()
        print("链接地址：", address)
        while True:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            text = data.decode()

            print("接收到的内容为：", text)

            conn.send(data)

        conn.close()

    ss.close()


if __name__ == "__main__":
    print("starting.......")
    tcp_server()
    print("ending......")