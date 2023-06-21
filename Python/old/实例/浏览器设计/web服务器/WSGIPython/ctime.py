'''显示当前时间'''

import time

def application(env, start_response):
    status_code = '200 OK'
    response_headers = [('Server', 'My Server')]

    start_response(status_code, response_headers)

    return time.ctime()