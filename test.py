from tkinter import *


root=Tk()
root.title("Fantasy Cricket")
root.geometry("680x420")
root.resizable(width=FALSE,height=FALSE)
# -----------Show Root win in center--------------
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# 3
def home(xxx):
    print(xxx)

#2
def NEW():
    xxx=1
    home(xxx)
def OPEN():
    xxx=2
    home(xxx)
def SAVE():
    xxx=3
    home(xxx)
def EVALUATE():
    xxx=4
    home(xxx)

#0
center(root)
#1
mb= Menubutton ( root, text="Manage Teams", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mb.config(background="#CCCCCC")
mb.menu.config(background="#CCCCCC")

mb.menu.add_command(label="NEW Team", command=NEW)
mb.menu.add_command(label="OPEN Team", command=OPEN)
mb.menu.add_command(label="SAVE Team", command=SAVE)
mb.menu.add_command(label="EVALUATE Team", command=EVALUATE)
mb.place(x=0,y=0)

labelframe = LabelFrame(root, text="Your Selection")
labelframe.place(x=45,y=45)

left = Label(labelframe, text="")
left.pack()
left = Label(labelframe, text="     Batsman(BAT)               "
                              "     Bowers(BOW)                 "
                              "     Allroundders(AR)             "
                              "     Wicket-Keeper(WK)                 ")
left.pack()
left = Label(labelframe, text="")
left.pack()

sbox1 = Text(labelframe, height=1, width=2, bg="white")
sbox1.place(x=97, y=23)
sbox1.tag_configure('color', foreground='#399B9B', font=('Calibri', 12, 'bold'))
sbox1.insert(END, "##", 'color')
sbox1.configure(state='disabled')
sbox2 = Text(labelframe, height=1, width=2, bg="white")
sbox2.place(x=230, y=23)
sbox2.tag_configure('color', foreground='#399B9B', font=('Calibri', 12, 'bold'))
sbox2.insert(END, "##", 'color')
sbox2.configure(state='disabled')
sbox3 = Text(labelframe, height=1, width=2, bg="white")
sbox3.place(x=386, y=23)
sbox3.tag_configure('color', foreground='#399B9B', font=('Calibri', 12, 'bold'))
sbox3.insert(END, "##", 'color')
sbox3.configure(state='disabled')
sbox4 = Text(labelframe, height=1, width=2, bg="white")
sbox4.place(x=544, y=23)
sbox4.tag_configure('color', foreground='#399B9B', font=('Calibri', 12, 'bold'))
sbox4.insert(END, "##", 'color')
sbox4.configure(state='disabled')



root.mainloop()