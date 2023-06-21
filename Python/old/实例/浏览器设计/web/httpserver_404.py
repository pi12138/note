# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:13:43 2017

@author: dc
"""

import http.server as hs
import sys, os


class ServerException(Exception):

    '''服务器内部错误'''

    pass

class case_no_file(object):
    
    def test(self, handler):
        
        pass
    
    
class RequestHandler(hs.BaseHTTPRequestHandler):
    
    def send_content(self, page, status = 200):
        
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, encoding = 'utf-8'))
        #print(page)
    
    
    def do_GET(self):
    #这里要处理两个异常，一个是读入路径时可能出现的异常，一个是读入路径后若不是文件，要作为异常处理    
        try:
            
            #获取文件路径
            full_path = os.getcwd() + self.path
            
                                 
            
            # 如果路径不存在
            if not os.path.exists(full_path):
                
                raise ServerException("'{0}' not found".format(self.path))
        
            #如果该路径是一个文件    
            elif os.path.isfile(full_path):
            
                self.handle_file(full_path)
        
            #如果该路径不是一个文件
            else:
            
                raise ServerException("Unknown object '{0}'".format(self.path))
            
        except Exception as msg:
        
            self.handle_error(msg)

    
    def handle_file(self, full_path):
        
        try:
            
            with open(full_path, 'r') as file:
                
                content = file.read()
                
                
            self.send_content(content,200)
            
        except IOError as msg:
            
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            
            self.handle_error(msg)
    
    Error_Page = """\
    <html>
    <body>
    <h1>Error accessing {path}</h1>
    <p>{msg}</p>
    </body>
    </html>
    """
            
    def handle_error(self, msg):
        
        content = self.Error_Page.format(path= self.path,msg= msg)
        
        self.send_content(content, 404)
            
        
        
        

if __name__ == '__main__': 
    
    httpAddress = ('', 8030)
    
    httpd = hs.HTTPServer(httpAddress, RequestHandler)
    
    httpd.serve_forever()