# tcp 服务端
socket = socket.socket()
socket.bind()
socket.listen()

while True:
	cli_socket = socket.accept()
    # 多进程
    p = Process(target = fun, args = ())
    p.start()
    cli_socket.close()
   

def fun(cli_socket):
	# 接收数据
	# request_data = recv()
	# print(request_data)
	# 解析HTTP报文数据，request_data
	# 提取请求方式
	# 提取请求路径
	# 返回响应格式

	'''
	HTTP/1.1 200 OK\r\n
	\r\n
	Hello Browser
	'''

	# send()
	# close()