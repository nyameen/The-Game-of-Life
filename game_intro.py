import socket
from random import randint
from tkinter import *
import _thread

def host():
    top = Toplevel()
    top.title("Host")
    top.minsize(width=350, height=250)

    msg = Label(top, text="Waiting for connection...")
    msg.pack()

    button = Button(top, text="Start", command=hostStart)
    button.pack()

def hostStart():
    s = socket.socket()
    host = socket.gethostname()
    port = 12221
    s.bind((host, port))

    s.listen(5)
    c = None

    print ('[Waiting for connection...]')
    c, addr = s.accept()
    print ('Got connection from', addr)


def clientStart(hostIp):
    port = 12221
    s = socket.socket()
    s.connect((hostIp, port))
    print('Connected to', host)

def client():
    top = Toplevel()
    top.title("Host")
    top.minsize(width=350, height=250)
    msg = Label(top, text="Please enter the host IP address")
    msg.pack()



    buttond = Button(top, text="ddds", command=lambda: clientStart("10.0.0.198"))
    buttond.pack()


    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

window = Tk()
window.wm_title("The Game of Life")
window.minsize(width=780, height=670)
window.maxsize(width=780, height=670)
window.config(bg="#0033cc")


topLab = Label(window, text="The Game of Life", bg="#0033cc", fg="white", font='Helvetica 44 bold')
topLab.pack()
topLab.place(x=135,y=55)

unLab = Label(window, text="Username:", bg="#0033cc", fg="white", font='Helvetica 20')
unLab.pack()
unLab.place(x=150,y=200)

unEntry = Entry(window, font='Helvetica 20')
unEntry.pack()
unEntry.place(x=300,y=200)

hostButton = Button(window, width=10, height=1, text="Host", command=host, font='Helvetica 40 bold')
hostButton.pack()
hostButton.place(x=210,y=300)

clientButton = Button(window, width=10, height=1, text="Client", command=client, font='Helvetica 40 bold')
clientButton.pack()
clientButton.place(x=210,y=450)

window.mainloop()
