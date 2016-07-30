# -*- coding:utf-8 -*-
import getpass
import socket
import Tkinter
import ttk
__author__ = 'BlackIce'


def log_in():
    """
    登录签到
    :param server_ip:
    :return:
    """
    # host = '127.0.0.1'    # The remote host
    server_ip = ip_addr.get()
    port = 2000
    data = getpass.getuser()

    try:
        # SOCK_DGRAM is the socket type to use for UDP sockets
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # As you can see, there is no connect() call; UDP has no connections.
        # Instead, data is directly sent to the recipient via sendto().
        sock.sendto(data + "@\n", (server_ip, port))
        received = sock.recv(1024)
        conn_status.set("连接成功")
        return_message.set(received)
    except socket.error:
        return_message.set('')
        conn_status.set("连接失败")


def log_out():

    server_ip = ip_addr.get()
    port = 2000
    data = getpass.getuser()
    try:
        # SOCK_DGRAM is the socket type to use for UDP sockets
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # As you can see, there is no connect() call; UDP has no connections.
        # Instead, data is directly sent to the recipient via sendto().
        sock.sendto(data + "*\n", (server_ip, port))
        received = sock.recv(1024)
        conn_status.set("连接成功")
        return_message.set(received)
    except socket.error:
        return_message.set('')
        conn_status.set("连接失败")


root = Tkinter.Tk()
root.title('test')
# root 大小不可变
root.resizable(False, False)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(Tkinter.N, Tkinter.W, Tkinter.E, Tkinter.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
ip_addr = Tkinter.StringVar()
return_message = Tkinter.StringVar()
conn_status = Tkinter.StringVar()

# 第一行所有内容
ttk.Label(mainframe, text="签到IP:").grid(column=1, row=1, sticky=Tkinter.E)
feet_entry = ttk.Entry(mainframe, width=15, textvariable=ip_addr)
feet_entry.grid(column=2, row=1, sticky=(Tkinter.W, Tkinter.E))
ttk.Label(mainframe, textvariable=conn_status).grid(column=3, row=1, sticky=(Tkinter.W, Tkinter.E))
# 第二行内容
ttk.Label(mainframe, textvariable=return_message).grid(column=2, row=2, sticky=(Tkinter.E, Tkinter.W))
# 第三行按钮
ttk.Button(mainframe, text="签到", command=log_in).grid(column=1, row=3, sticky=Tkinter.E)
ttk.Button(mainframe, text="签退", command=log_out).grid(column=3, row=3, sticky=Tkinter.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    feet_entry.focus()
    root.bind('<Return>', log_in)
root.mainloop()
