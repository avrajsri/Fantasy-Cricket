from tkinter import *


root=Tk()
root.title("Fantasy Cricket")
root.geometry("600x370")
root.resizable(width=FALSE,height=FALSE)
# -----------Show Root win in center--------------
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#2
def NEW():
    print("NEW Team")
def OPEN():
    print("OPEN Team")
def SAVE():
    print("SAVE Team")
def EVALUATE():
    print("EVALUATE Team")

#0
center(root)
#1
mb= Menubutton ( root, text="Manage Teams", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

selected = IntVar()
mb.menu.add_command(label="NEW Team", command=NEW)
mb.menu.add_command(label="OPEN Team", command=OPEN)
mb.menu.add_cascade(label="SAVE Team", command=SAVE)
mb.menu.add_cascade(label="EVALUATE Team", command=EVALUATE)
mb.place(x=0,y=0)


root.mainloop()