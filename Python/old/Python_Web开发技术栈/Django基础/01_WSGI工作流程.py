from wsgiref.simple_server import make_server

def application(environ, start_response):
	start_response("200 OK", [('Content-Type', 'text/html')])

	return [b'<h1>Hello, web!</h1>']


class WebApp:
	def __init__(self):
		pass

	def __call__(self, environ, start_response):
		start_response("200 OK", [('Content-Type', 'text/html')])

		return [b'<h1>Hello, web app!</h1>']

	def listen(self, port):
		httpd = make_server("", port, self)
		print("server start on port {}.....".format(port))
		httpd.serve_forever()


if __name__ == "__main__":
	# httpd = make_server("", 9999, application)
	# print("server start on port 9999.....")
	# httpd.serve_forever()

	web = WebApp()
	web.listen(9999)