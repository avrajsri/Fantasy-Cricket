from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Fantasy Cricket")
root.geometry("680x420")
root.resizable(width=FALSE, height=FALSE)
root.configure(background='#FFFFFF')

# -----------Show Root win in center--------------
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#4
def go(event):
    pass

#3
def selection():
    c.execute("SELECT player, ctg FROM data")
    data = c.fetchall()
    for i in data:
        c.execute("INSERT INTO "+tn+"(player, Tin, Tout, ctg) VALUES (?, ?, ?, ?)", (i[0], int(0), int(1), i[1]))
        conn.commit()

    s = selected.get()
    print(s)


#2
def NEW():
    def tname():
        global tn
        tn=en.get()
        tnl=len(tn)
        if(tnl==0 or tnl==""):
            pass

        else:
            root1.destroy()

            try:
                global conn
                global c
                conn = sqlite3.connect('Cricket.db')
                c = conn.cursor()

                c.execute("CREATE TABLE "+tn+"(player TEXT, Tin INTEGER, Tout INTEGER, ctg TEXT)")
                conn.commit()

                c.execute("INSERT INTO TeamData(NewTeam, Point) VALUES (?, ?)",(tn,int(0)))
                conn.commit()

                e1.configure(text=0)
                e2.configure(text=0)
                e3.configure(text=0)
                e4.configure(text=0)
                e5.configure(text=1000)
                e6.configure(text=0)
                e7.configure(text=tn)

                rad1.configure(state='active')
                rad2.configure(state='active')
                rad3.configure(state='active')
                rad4.configure(state='active')

            except Exception as e:
                rad1.configure(state='disabled')
                rad2.configure(state='disabled')
                rad3.configure(state='disabled')
                rad4.configure(state='disabled')
                e1.configure(text="##")
                e2.configure(text="##")
                e3.configure(text="##")
                e4.configure(text="##")
                e5.configure(text="####")
                e6.configure(text="####")
                e7.configure(text="Displayed Here")

                messagebox.showwarning("Value Error", str(e))

    root1 = Tk()
    root1.title("Team Name")
    root1.geometry("380x200")
    root1.resizable(width=FALSE, height=FALSE)

    Label(root1, text="Enter Team Name: ", font=('Comic Sans MS', 12)).place(x=30, y=40)
    en = Entry(root1, font=('arial', 12, "bold"), bg="#F0F0F0", bd=5, highlightthickness=2, highlightcolor="black")
    en.focus_set()
    en.place(x=180, y=40, width=150)

    b1=Button(root1, text="OK", font=('Comic Sans MS', 10), relief=RAISED, bd=3, width=10, command=tname)
    b1.place(x=80, y=110)
    b2=Button(root1, text="Exit", font=('Comic Sans MS', 10), relief=RAISED, bd=3, width=10, command=root1.destroy)
    b2.place(x=220, y=110)

    center(root1)
    root1.mainloop()

def OPEN():
    pass

def SAVE():
    pass

def EVALUATE():
    pass

#1
mb= Menubutton (root, text="  Manage Teams  ",font=('Comic Sans MS',9),activebackground="#CCCCCC", relief="solid")
mb.place(x=0,y=0)
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mb.config(background="#CCCCCC")
mb.menu.config(background="#CCCCCC")

mb.menu.add_command(label="NEW Team", command=NEW,font=('Comic Sans MS',9))
mb.menu.add_command(label="OPEN Team", command=OPEN,font=('Comic Sans MS',9))
mb.menu.add_command(label="SAVE Team", command=SAVE,font=('Comic Sans MS',9))
mb.menu.add_command(label="EVALUATE Team", command=EVALUATE,font=('Comic Sans MS',9))
mb.place(x=0,y=0)

b1 = Text(root, height=4, width=72,bg="#F0F0F0", relief="solid")
b1.place(x=45,y=45)
b1.configure(state='disabled')

Label(b1, text="Your Selection",font=('Comic Sans MS',8)).place(x=1,y=0)
l1=Label(b1,text="Batsman (BAT)",font=('Comic Sans MS',9,"bold"))
l2=Label(b1,text="Bowers (BOW)",font=('Comic Sans MS',9,"bold"))
l3=Label(b1,text="Allroundders (AR)",font=('Comic Sans MS',9,"bold"))
l4=Label(b1,text="Wicket-Keeper (WK)",font=('Comic Sans MS',9,"bold"))
l1.place(x=3,y=23)
l2.place(x=138,y=23)
l3.place(x=273,y=23)
l4.place(x=420,y=23)


e1=Label(b1,text="##",font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B')
e1.place(x=97, y=26,width=15)
e2=Label(b1,text="##",font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B')
e2.place(x=230, y=26,width=15)
e3=Label(b1,text="##",font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B')
e3.place(x=382, y=26,width=15)
e4=Label(b1,text="##",font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B')
e4.place(x=546, y=26,width=15)


Label(root,text="Point Available",bg="white",font=('Comic Sans MS',9,"bold")).place(x=120,y=120)
Label(root,text="Point Used",bg="white",font=('Comic Sans MS',9,"bold")).place(x=430,y=120)

e5=Label(root,text="####",bg="white",font=('arial',10,"italic","bold"), fg='#399B9B')
e5.place(x=212, y=120)
e6=Label(root,text="####",bg="white",font=('arial',10,"italic","bold"),fg='#399B9B')
e6.place(x=500, y=120)

b1 = Text(root, height=15, width=28, bg="white", relief="solid")
b1.place(x=80, y=150)
b1.configure(state='disabled')
b2 = Text(root, height=15, width=28, bg="white", relief="solid")
b2.place(x=380, y=150)
b2.configure(state='disabled')

Label(root,text=">",bg="white", font=('Comic Sans MS',20)).place(x=335,y=245)
Label(root,text="Team Name: ", bg="white", font=('Comic Sans MS',10)).place(x=405,y=155)
e7=Label(root,text="Displayed Here", font=('arial',10,"bold"),bg="white", fg='#399B9B')
e7.place(x=485, y=156,width=100)

selected = IntVar()
rad1 = Radiobutton(root, text='BAT', value=1, bg="white",activebackground="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad2 = Radiobutton(root, text='BOW', value=2, bg="white",activebackground="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad3 = Radiobutton(root, text='AR', value=3, bg="white",activebackground="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad4 = Radiobutton(root, text='WK', value=4, bg="white",activebackground="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad1.place(x=85, y=155)
rad2.place(x=143, y=155)
rad3.place(x=207, y=155)
rad4.place(x=256, y=155)
rad1.configure(state='disabled')
rad2.configure(state='disabled')
rad3.configure(state='disabled')
rad4.configure(state='disabled')

#0
center(root)
root.mainloop()