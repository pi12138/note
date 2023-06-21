import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

sc.connect((host, port))


while True:
	send_msg = input('请输入你想输入的内容:')
	if len(send_msg) == 0:
		continue

	sc.send(send_msg.encode('utf-8'))

	recv_msg = sc.recv(1024)
	print('服务器接受的内容为:{0}'.format(recv_msg))

sc.close()

