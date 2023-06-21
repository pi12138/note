import socket
from io import StringIO
import sys


class WSGIWebServer(object):

	address_family = socket.AF_INET
	socket_type = socket.SOCK_STREAM
	request_queue_size = 1

	def __init__(self, server_address):
		listen_socket = socket.socket(self.address_family, self.socket_type)
		self.listen_socket = listen_socket

		# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listen_socket.bind(server_address)
		listen_socket.listen(self.request_queue_size)

		host, port = self.listen_socket.getsockname()[:2]
		self.server_name = socket.getfqdn(host)
		self.server_port = port
		self.headers_set = []

	def set_app(self, application):
		self.application = application

	def serve_forever(self):
		listen_socket = self.listen_socket
		while True:
			self.client_connection, client_address = listen_socket.accept()
			self.handle_one_request()

	def handle_one_request(self):
		request_data = self.client_connection.recv(1024)
		# request data: b'GET /hello HTTP/1.1\r\nUser-Agent: PostmanRuntime/7.15.0\r\nAccept: */*\r\nCache-Control: no-cache\r\nPostman-Token: 6a6fe679-91f1-47c5-a552-a18fbe3a4ab0\r\nHost: 127.0.0.1:8888\r\ncookie: csrftoken=HbFGrunbiXo6U0RSHthr46cEjYUjeQHz\r\naccept-encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
		self.request_data = request_data
		self.parse_request(request_data)
		env = self.get_environ()
		result = self.application(env, self.start_response)
		self.finish_response(result)

	def parse_request(self, data):
		format_data = data.splitlines()
		# print("format data: {}".format(format_data))
		# [b'GET /hello HTTP/1.1', b'User-Agent: PostmanRuntime/7.15.0', b'Accept: */*', b'Cache-Control: no-cache', b'Postman-Token: 541fef83-3d65-4d42-8840-7ffbe8996b36', b'Host: 127.0.0.1:8888', b'cookie: csrftoken=HbFGrunbiXo6U0RSHthr46cEjYUjeQHz', b'accept-encoding: gzip, deflate', b'Connection: keep-alive', b'']
		if len(format_data):
			request_line = data.splitlines()[0]
			# print(request_line)
			request_line = request_line.decode().rstrip('\r\n')
			(self.request_method, self.path, self.request_version) = request_line.split()
			# GET /hello HTTP/1.1

	def get_environ(self):
		env = {}
		env['wsgi.version'] = (1, 0)
		env['wsgi.url_scheme'] = 'http'
		env['wsgi.input'] = StringIO(self.request_data.decode())
		env['wsgi.errors'] = sys.stderr
		# print("sys.stderr: {}".format(sys.stderr))
		# sys.stderr: <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
		env['wsgi.multithread'] = False
		env['wsgi.multiprocess'] = False
		env['wsgi.run_once'] = False
		# Required CGI variables
		env['REQUEST_METHOD'] = self.request_method    	# GET
		env['PATH_INFO'] = self.path              		# /hello
		env['SERVER_NAME'] = self.server_name       	# localhost
		env['SERVER_PORT'] = str(self.server_port)  	# 8888
		
		return env

	def start_response(self, status, response_headers, exc_info=None):
		server_headers = [('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'), ('Server', 'WSGIServer 0.2')]
		self.headers_set = [status, response_headers + server_headers]

	def finish_response(self, result):
		try:
			status, response_headers = self.headers_set
			response = "HTTP/1.1 {status}\r\n".format(status=status)
			for header in response_headers:
				response += "{0}: {1}\r\n".format(*header)
			response += "\r\n"

			for data in result:
				response += data.decode()

			self.client_connection.sendall(response.encode())
			print(''.join('> {line}\n'.format(line=line) for line in response.splitlines()))
		finally:
			self.client_connection.close()


SERVER_ADDRESS = (HOST, PORT) = "", 8888

def make_server(serve_address, application):
	server = WSGIWebServer(SERVER_ADDRESS)
	server.set_app(application)

	return server

if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) < 2:
		sys.exit("Provide a WSGI application object as module:callable")
	app_path = sys.argv[1]
	module, application = app_path.split(":")
	module = __import__(module)
	application = getattr(module, application)

	httpd = make_server(SERVER_ADDRESS, application)
	print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
	httpd.serve_forever()
