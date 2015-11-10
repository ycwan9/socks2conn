# -*- coding: utf-8 -*-
import BaseHTTPServer
import SocketServer
import proxy
import socks
class ThreadingHTTPServer (SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer): pass

if __name__ == '__main__':
    print 'hello'
    from sys import argv
    if len(argv)<2 or argv[1] in ('-h', '--help'):
        print argv[0], "socks_sever:port [port]"
    else:
        socks_host, socks_port = argv[1].split(":")
        socks_port = int(socks_port)
        proxy.set_socks(socks.PROXY_TYPE_SOCKS5, socks_host, socks_port)
        port = 8080
        if argv[2:]:
            port = int(argv[1])
        print "listen on %i"%port
        httpd = ThreadingHTTPServer(('0.0.0.0',port), proxy.proxy)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print 'bye bye\nExit by Keyboard Interrupt'