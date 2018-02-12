import socket
from random import randint
from tkinter import *
import _thread

def host():
    top = Toplevel()
    top.title("Host")
    top.minsize(width=350, height=250)
    msg = Label(top, text="You are hosting a game.")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

def client():
    pass;

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
