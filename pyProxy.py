# -*- coding: utf-8 -*-
import BaseHTTPServer
import proxy

if __name__ == '__main__':
    print 'hello'
    from sys import argv
    if argv[2:] and argv[1] in ('-h', '--help'):
        print argv[0], "socks_sever:port [port]"
    else:
        port = 8080
        if argv[1:]:
            port = int(argv[1])
        class ThreadingHTTPServer (SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer): pass
        print "listen on %i"%port
        httpd = ThreadingHTTPServer(('0.0.0.0',port), proxy.proxy)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print 'bye bye\nExit by Keyboard Interrupt'