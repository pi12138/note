from socketserver import TCPServer, StreamRequestHandler
from time import ctime


HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequesrHandler(StreamRequestHandler):
    def handle(self):
        print("...connected from: {}".format(self.client_address))
        self.wfile.write('[{}] {}'.format(ctime(), self.rfile.readline().decode()).encode())


tcp_serv = TCPServer(ADDR, MyRequesrHandler)
print('waiting for connection...')
tcp_serv.serve_forever()