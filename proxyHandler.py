# -*- coding: utf-8 -*-
import BaseHTTPServer, select, socket
import proxy
import debug_server

    #__base = BaseHTTPServer.BaseHTTPRequestHandler
    #__base_handle = __base.handle

class ProxyHandler (BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = "PyProxy/0.1"
    rbufsize = 0                        # self.rfile Be unbuffered

    def do_CONNECT(self):
        netloc = self.path
        i = netloc.find(':')
        if i >= 0:
            self.host_and_port = netloc[:i], int(netloc[i+1:])
        else:
            self.host_and_port = netloc, 80
        try:
            print "\t" "connect to %s:%d" %self.host_and_port
            self.log_request(200)
            self.do_ssl_rw()
        finally:
            print "\t" "bye"
            self.connection.close()