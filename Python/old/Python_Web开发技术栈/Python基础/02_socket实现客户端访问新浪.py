import socket


def func():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('www.sina.com.cn', 80))
	s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

	buffer = []

	while True:
		data = s.recv(1024)
		if data:
			buffer.append(data)
		else:
			break

	data = b"".join(buffer).decode()

	s.close()

	write_file(data)


def write_file(data):
	header, html = data.split('\r\n\r\n')

	with open('sina.html', 'w') as f:
		f.write(html)


if __name__ == "__main__":
	func()