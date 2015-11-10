# -*- coding: utf-8 -*-
import select
import proxyHandler
import socks

def set_socks(stype, shost, sport):
    socks.setdefaultproxy(stype, shost, sport)
    
class proxy(proxyHandler.ProxyHandler): 
    def tunnel(self, max_idling=20):
        print "reading & writing %s on port %i"%self.host_and_port
        try:
            soc = socks.socksocket()
            soc.connect(self.host_and_port)
            self.wfile.write(self.protocol_version +
                             " 200 Connection established\r\nProxy-agent: %s\r\n\r\n"%self.version_string())
            count = 0
            istr = '' #the input of the client's data log
            ostr = '' #the server's input(output to the client) data log
            while 1:
                count += 1
                (ins, _, exs) = select.select((soc, self.connection), (), (soc, self.connection), 3)
                if exs: break
                if ins:
                    for i in ins:
                        if i is soc:
                            data = i.recv(8192)
                            if data:
                                self.connection.send(data)
                                ostr += data
                                count = 0
                            #ostr
                        else:
                            data = i.recv(8192)
                            if data:
                                soc.send(data)
                                istr += data
                                count = 0
                            #istr
                else:
                    print "\t" "idle", count
                if count == max_idling: break
        except socket.timeout:
            print "time out, done."
            return 0
        except (socket.error,socket.herror),err:
            print "Err :%s"%repr(err)
            return 1
        return 0