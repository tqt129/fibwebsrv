#!/usr/bin/env python2.7

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self.fibonacci(self.path))

    def fibonacci(self, x):
        myFiboUrl = x.split('/fib/')
        myFiboNumber = int(myFiboUrl[-1])
        if myFiboNumber <= 0:
            return ('invalid entry')
        else:
            List = []
            a, b = 0, 1
            for i in range(myFiboNumber):
                List.append(a)
                a,b = b, a+b
            return List
     
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

