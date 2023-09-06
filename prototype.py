import tkinter.ttk
from tkinter import *

# Set up
mainwindow = Tk()
mainwindow.geometry("200x100")

inputcalc = tkinter.ttk.Entry(mainwindow)



def changepage(current: Frame, future: Frame):
    current.forget()
    future.pack()
    mainwindow.update_idletasks()


test1frame = Frame(mainwindow)
test1 = Button(test1frame, text="Next")
test1.pack()
test1frame.pack()

test2frame = Frame(mainwindow)
test2 = Button(test2frame, text="GO Back")
test2.pack()

test1.config(command=lambda: changepage(test1frame, test2frame))
test2.config(command=lambda: changepage(test2frame, test1frame))



mainwindow.mainloop()