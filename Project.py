from tkinter import *

window = Tk()

window.title("Math Project")

window.geometry('350x200')

PLbl = Label(window, text="Pressure")
PLbl.grid(column=0, row=0)

P = Entry(window,width=10)
P.grid(column=1, row=0)

nlbl = Label(window, text="Pump efficiency")
nlbl.grid(column=0, row=2)

n = Entry(window,width=10)
n.grid(column=1, row=2)

Hlbl = Label(window, text="Head")
Hlbl.grid(column=0, row=3)

H = Entry(window,width=10)
H.grid(column=1, row=3)

rlbl = Label(window, text="Resistance of the fluid being pumped")
rlbl.grid(column=0, row=4)

r = Entry(window,width=10)
r.grid(column =1, row=4)

def clicked():

    res = "Flow Rate = " + str (float(P.get())*float(n.get())*(1-(float(r.get())/(float(r.get())+float(H.get())))))

    resultLabel.configure(text= res)

btn = Button(window, text="calculate flow rate", command=clicked)

btn.grid(column=1, row=5)

resultLabel = Label(window, text="Flow Rate")
resultLabel.grid(column=0, row=6)

window.mainloop()