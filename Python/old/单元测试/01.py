# 服务器文件
import socket


class MyServer(object):
	def __init__(self, host="127.0.0.1", port=9999):
		self.host = host
		self.port = port
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		

	def run_server(self):
		self.server.bind((self.host, self.port))
		self.server.listen(5)
		print("server is running....")
		while True:
			client_obj, client_address = self.server.accept()
			print("{}已连接...".format(client_address))

			request_data = client_obj.recv(1024)
			for i in request_data.decode().splitlines():
				print(i)
			request_line = request_data.decode().splitlines()[0]
			request_method, request_path, request_version = request_line.split()
			response_data = ""
			
			if request_method == "GET": 
				response_line = "HTTP/1.1 200 OK\r\n"
				response_header = "Server: MyServer\r\n"
				response_body = "GET success"
				response_data = response_line + response_header + "\r\n" + response_body
			elif request_method == "POST":
				response_line = "HTTP/1.1 200 OK\r\n"
				response_header = "Server: MyServer\r\n"
				response_body = "POST success"
				response_data = response_line + response_header + "\r\n" + response_body

			client_obj.send(response_data.encode())
			client_obj.close()

		self.close_server()

	def close_server(self):
		self.server.close()


if __name__ == "__main__":
	ser = MyServer()
	ser.run_server()