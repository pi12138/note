import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

connect, address = ss.accept()

while True:
	print("收到来自{0}的信息".format(address))

	recv_msg = connect.recv(1024)
	if len(recv_msg) == 0:
		break

	print("信息内容为:{0}".format(recv_msg))

	connect.send(recv_msg)

connect.close()

ss.close

