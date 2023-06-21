
import time

HTML_ROOT_DIR = './html'


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get('FILE_NAME', '/')
        print("path:", path)

        if path.startswith('/static'):
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, 'rb')
            except:
                status_code = '404 Not Found'
                response_headers = [('Server', 'My Server')]
                start_response(status_code, response_headers)
                return 'Not Found File'
            else:
                content = file.read()
                file.close()

            status_code = '200 OK'
            response_headers = [('Server', 'My Server')]
            start_response(status_code, response_headers)
            return content.decode('utf-8')

        else:
            for url, handler in self.urls:
                if url == path:
                    print('handler:', handler)
                    return handler(env, start_response)
                # 如果未在Urls中找到需要信息，则返回404
                status_code = '404 Not Found'
                response_headers = [('Server', 'My Server')]
                start_response(status_code, response_headers)
                return 'Not Found File'


def handle_time(env, start_response):
    status_code = '200 OK'
    response_headers = [('Server', 'My Server')]

    start_response(status_code, response_headers)

    return time.ctime()


def handle_sayhello(env, start_response):
    status_code = '200 OK'
    response_headers = [("Server", 'My Server')]

    start_response(status_code, response_headers)

    return "hello world"


urls = [
    ('/ctime', handle_time),
    ('/sayhello', handle_sayhello)
]

app = Application(urls)