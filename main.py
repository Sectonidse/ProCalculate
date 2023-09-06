"""
\____________________________________________________________________________________________________
| Secton's                                                                                           \
|                                                                                                     \
| _____  _____   _______ _______ _______ ___      _______ ___   ___ ___      _______ _______ _______   \
| |    \ |    \  | ___ | |  ___| | ___ | | |      |  ___| | |   | | | |      | ___ | |__ __| | ____|    \
| | __/  |    /  | | | | | |     | |_| | | |      | |     | |   | | | |      | |_| |   | |   | |_       /
| | |    | |\ \  | |_| | | |___  | ___ | | |____  | |___  | |___| | | |____  | ___ |   | |   | __|_    /
| |_|    |_| \_\ |_____| |_____| |_| |_| |______| |_____| |_______| |______| |_| |_|   |_|   |_____|  /
|                                                                                                    /
|___________________________________________________________________________________________________/
|          Just another digital calculator... Feel free to contribute for a new feature!           |
|__________________________________________________________________________________________________|
"""
import tkinter.ttk
from tkinter import *

# Set up
mainwindow = Tk()
mainwindow.title("ProCalculate")
mainwindow.geometry("350x150")
mainwindow.minsize(350, 150)
calculation = Variable()
mainframe = tkinter.ttk.Frame(mainwindow)
inputcalc = tkinter.ttk.Entry(mainframe, state="disabled", textvariable=calculation)
inputcalc.grid(row=1, column=1, columnspan=4, ipadx=50)

# Menu
mainmenu = Menu(mainwindow)

calctypes = Menu(mainmenu, tearoff=0)
calctypes.add_command(label="Simple")
calctypes.add_command(label="Advanced")
calctypes.add_command(label="Maximal")
calctypes.add_command(label="Binary")
mainmenu.add_cascade(menu=calctypes, label="Type")

mainmenu.add_checkbutton(label="History")



# Functions
symbolics: str
def insertcalc():
    global symbolics
    if mainframe.focus_get()["text"] == "+" or mainframe.focus_get()["text"] == "-" or mainframe.focus_get()["text"] == "/" or mainframe.focus_get()["text"] == "*":
        calculation.set(calculation.get() + " " + mainframe.focus_get()["text"] + " ")
    elif mainframe.focus_get()["text"] == "Solve":
        calculation.set(str(eval(calculation.get())))
    else:
        calculation.set(calculation.get() + mainframe.focus_get()["text"])
    inputcalc.update()

def clearvar(): calculation.set(""); inputcalc.update()


# Numbers
num1 = tkinter.ttk.Button(mainframe, text="1", command=insertcalc)
num1.grid(row=4, column=1)
num2 = tkinter.ttk.Button(mainframe, text="2", command=insertcalc)
num2.grid(row=4, column=2)
num3 = tkinter.ttk.Button(mainframe, text="3", command=insertcalc)
num3.grid(row=4, column=3)
num4 = tkinter.ttk.Button(mainframe, text="4", command=insertcalc)
num4.grid(row=3, column=1)
num5 = tkinter.ttk.Button(mainframe, text="5", command=insertcalc)
num5.grid(row=3, column=2)
num6 = tkinter.ttk.Button(mainframe, text="6", command=insertcalc)
num6.grid(row=3, column=3)
num7 = tkinter.ttk.Button(mainframe, text="7", command=insertcalc)
num7.grid(row=2, column=1)
num8 = tkinter.ttk.Button(mainframe, text="8", command=insertcalc)
num8.grid(row=2, column=2)
num9 = tkinter.ttk.Button(mainframe, text="9", command=insertcalc)
num9.grid(row=2, column=3)
num0 = tkinter.ttk.Button(mainframe, text="0", command=insertcalc)
num0.grid(row=5, column=2)

# Other Buttons 2
plus = tkinter.ttk.Button(mainframe, text="+", command=insertcalc)
plus.grid(row=2, column=4)
minus = tkinter.ttk.Button(mainframe, text="-", command=insertcalc)
minus.grid(row=3, column=4)
mul = tkinter.ttk.Button(mainframe, text="*", command=insertcalc)
mul.grid(row=4, column=4)
div = tkinter.ttk.Button(mainframe, text="/", command=insertcalc)
div.grid(row=5, column=4)

# Other Buttons
clearbut = tkinter.ttk.Button(mainframe, text="Clear", command=clearvar)
clearbut.grid(row=5, column=1)
solvebut = tkinter.ttk.Button(mainframe, text="Solve", command=insertcalc)
solvebut.grid(row=5, column=3)



# Let this be always at the end of script.
mainframe.pack(fill="both", expand=True)
mainwindow.config(menu=mainmenu)
mainwindow.mainloop()