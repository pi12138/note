import socket

def clientfunc():
    sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = 'This is a msg'

    # 发送的信息必须是bytes格式的
    data = text.encode()

    host = socket.gethostname()
    port = 9999

    # 发送消息到相应ip和端口号的地址
    sc.sendto(data, (host, port))

    data, addr = sc.recvfrom(500)

    text = data.decode()

    print('接受到的反馈信息：', text)

if __name__ == '__main__':
    clientfunc()