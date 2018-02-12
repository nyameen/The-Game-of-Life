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

w = Canvas(window, width=780, height=670, bg ="#0033cc")
w.pack()

topLab = Label(text="The Game of Life", bg="#0033cc", fg="white", font='Helvetica 44 bold')
topLab.pack()
topLab.place(x=135,y=55)

unEntry = Entry(w, width=10, font='Helvetica 20')
unEntry.place()
unEntry.pack(x=200,y=60)

hostButton = Button(w, width=10, height=1, text="Host", command=host, font='Helvetica 40 bold')
hostButton.pack()
hostButton.place(x=210,y=300)

clientButton = Button(w, width=10, height=1, text="Client", command=client, font='Helvetica 40 bold')
clientButton.pack()
clientButton.place(x=210,y=450)

w.mainloop()
