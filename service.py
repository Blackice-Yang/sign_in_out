# -*- coding:utf-8 -*-
__author__ = 'BlackIce'
import socket
import datetime


def message():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 2000              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while 1:
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            print data
            print datetime.datetime.now()
            conn.sendall('Bye')
        conn.close()


if __name__ == '__main__':
    message()
