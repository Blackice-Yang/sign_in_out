# -*- coding:utf-8 -*-
__author__ = 'BlackIce'
import SocketServer
import datetime


class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print str(datetime.datetime.now())
        print "i am {}".format(data[:-1])
        if data.endswith('@'):
            socket.sendto("上班", self.client_address)
        else:
            socket.sendto("下班", self.client_address)


if __name__ == "__main__":
    HOST, PORT = "", 2000
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
