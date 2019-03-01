from tkinter import *


root=Tk()
root.title("Fantasy Cricket")
root.geometry("680x420")
root.resizable(width=FALSE,height=FALSE)
root.configure(background='#FFFFFF')
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
mb.place(x=0,y=0)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mb.config(background="#CCCCCC")
mb.menu.config(background="#CCCCCC")

mb.menu.add_command(label="NEW Team", command=NEW)
mb.menu.add_command(label="OPEN Team", command=OPEN)
mb.menu.add_command(label="SAVE Team", command=SAVE)
mb.menu.add_command(label="EVALUATE Team", command=EVALUATE)
mb.place(x=0,y=0)

fm = Frame(root, borderwidth=2, relief="groove")
fm.place(x=45,y=45)

Label(fm, text="Your Selection").place(x=1,y=1)

Label(fm, text="").pack()
Label(fm, text="     Batsman(BAT)               "
                              "     Bowers(BOW)                 "
                              "     Allroundders(AR  )             "
                              "     Wicket-Keeper(WK)                 ").pack()
Label(fm, text="").pack()

l=Label(fm,text="     Batsman(BAT)               "
                              "     Bowers(BOW)                 "
                              "     Allroundders(AR)             "
                              "     Wicket-Keeper(WK)")
l.place(x=0,y=25)

z=StringVar()
z.set("##")
#z.initialize("##")

e1=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z)
e1.place(x=97, y=26,width=15)
e2=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z)
e2.place(x=230, y=26,width=15)
e3=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z)
e3.place(x=386, y=26,width=15)
e4=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z)
e4.place(x=544, y=26,width=15)

#e1.configure(state='disabled')
#e2.configure(state='disabled')
#e3.configure(state='disabled')
#e4.configure(state='disabled')




root.mainloop()