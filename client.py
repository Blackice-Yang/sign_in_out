# -*- coding:utf-8 -*-
__author__ = 'BlackIce'
import socket
import getpass
import Tkinter


def message():
    HOST = '127.0.0.1'    # The remote host
    PORT = 2000              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendall(getpass.getuser())
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)


class Application(Tkinter.Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def say_bye(self):
        print "hi there, everyone!"

    def create_widgets(self):
        self.QUIT = Tkinter.Button(self)
        self.QUIT["text"] = "签到"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.say_hi

        self.QUIT.pack({"side": "left"})

        self.hi_there = Tkinter.Button(self)
        self.hi_there["text"] = "签退",
        self.hi_there["command"] = self.say_bye

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


def gui_pad():
    """
    配置一个gui面板
    :return:
    """
    tt = Tkinter.Tk()
    app = Application(master=tt)
    app.master.title('我要签到')
    app.master.minsize(180, 50)
    app.mainloop()

if __name__ == '__main__':
    gui_pad()
