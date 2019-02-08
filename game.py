import socket
from random import randint
from tkinter import *
import _thread

global turn
turn = 1

# Make new tkinter oage for connect/host screen
# test commit

def hitMiss():
    c.send(("<ack>1</ack>").encode())

def receiving():
    global turn
    data = ""
    while(1):
        data = data + str(c.recv(1),'utf-8')
        if "</coord>" in data:
            datarec = data[7:data.find("</coord>")]
            print(datarec)
            data = ""
            hitMiss()
            turn = 1
        elif "</ack>" in data:
            datarec = data[5:data.find("</ack>")]
            print(datarec)
            data = ""
            

def click(row, col):
    global turn
    if turn == 1:
        c.send(("<coord>" + str(row) + "," + str(col) + "</coord>").encode())
        turn = 0
    
window = Tk()
window.wm_title("The Game of Life")
window.minsize(width=780, height=670)
window.maxsize(width=780, height=670)
w = Canvas(window, width=780, height=670, bg ="#0033cc")
w.pack()
#w.create_rectangle(10, 10, 330, 330, fill="red")
#w.create_rectangle(10, 340, 330, 660, fill="red")

topLabel = Label(text="A      B      C     D      E      F      G      H      I      J  ",
                 bg ="#0033cc", fg = "white")
topLabel.pack()
topLabel.place(x = 40, y = 20)

i = 0
yy = 40
while i < 10:
    number = str(i+1)
    leftLabel = Label(text=number, bg ="#0033cc", fg = "white")
    leftLabel.pack()
    leftLabel.place(x = 20, y = yy)
    yy = yy + 25
    i = i + 1

butList = []
for row in range(10):
    for col in range(10):
        button = Button(w, width=2, command=lambda row=row, col=col: click(row, col))
        butList.append(button)
        button.pack()
        button.place(x = (40+(24*col)), y = (40+(25*row)))


butList[21].configure(bg="red")
butList[31].configure(bg="cyan")


#s = socket.socket()
host = socket.gethostname()
port = 12221
#s.bind((host, port))

#s.listen(5)
c = None

print ('[Waiting for connection...]')
#c, addr = s.accept()
print ('Got connection from', addr)


try:
   _thread.start_new_thread(receiving, ())
except:
   print("Error: unable to start thread")

window.mainloop()




