from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read().encode())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))


def main():
    try:
        server = HTTPServer(('', 8888), MyHandler)
        print('Welcome to the machine...')
        print('Press ^C once or twice to quit.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == "__main__":
    main()