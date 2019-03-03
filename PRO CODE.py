from tkinter import *
import sqlite3

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

#$
def show(u):

    titleList1 = Listbox(root, font=('Comic Sans MS', 12), listvariable=u, highlightcolor="white", bd=0, width=22,
                         height=6, fg="#497CFF", selectbackground="#CCFFFF", selectforeground="#497CFF")
    titleList1.focus_set()
    for t in u:
        titleList1.insert(END, t)
    titleList1.place(x=83, y=200)


#3
def selection():
    s = selected.get()
    global conn
    global c
    conn = sqlite3.connect('Cricket.db')
    c = conn.cursor()

    if(s==1):
        c.execute("SELECT player FROM data WHERE ctg = ?", ["BAT"])
        data = c.fetchall()

        a = []
        for i in data:
            #print(i[0])
            a.append(i)
        show(a)


    elif(s==2):
        c.execute("SELECT player FROM data WHERE ctg = ?", ["BOW"])
        data = c.fetchall()

        a = []
        for i in data:
            #print(i[0])
            a.append(i)
        show(a)


    elif(s==3):
        c.execute("SELECT player FROM data WHERE ctg = ?", ["AR"])
        data = c.fetchall()

        a = []
        for i in data:
            #print(i[0])
            a.append(i)
        show(a)


    else:
        c.execute("SELECT player FROM data WHERE ctg = ?", ["WK"])
        data = c.fetchall()

        a = []
        for i in data:
            #print(i[0])
            a.append(i)
        show(a)

#2
def NEW():

    def tname():
        tn=e.get()
        tnl=len(tn)
        if(tnl==0 or tnl==" "):
            pass

        else:
            root1.destroy()

            z1.set("0")
            z2.set("0")
            z3.set("0")
            z4.set("0")
            zz1.set("1000")
            zz2.set("0")
            zzz.set(tn)

            rad1.configure(state='active')
            rad2.configure(state='active')
            rad3.configure(state='active')
            rad4.configure(state='active')

    root1 = Tk()
    root1.title("Team Name")
    root1.geometry("380x200")
    root1.resizable(width=FALSE, height=FALSE)

    Label(root1, text="Enter Team Name: ", font=('Comic Sans MS', 12)).place(x=30, y=40)
    e = Entry(root1, font=('arial', 11, "italic"), bg="#F0F0F0", bd=5, highlightthickness=2, highlightcolor="black",
              fg='#399B9B')
    e.focus_set()
    e.place(x=180, y=40)

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
mb= Menubutton ( root, text="Manage Teams",font=('Comic Sans MS',9), relief=RAISED )
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

fm = Frame(root, borderwidth=2, relief="groove")
fm.place(x=45,y=45)

Label(fm, text="Your Selection",font=('Comic Sans MS',8)).place(x=1,y=0)

Label(fm, text="").pack()
Label(fm, text="     Batsman(BAT)               "
               "     Bowers(BOW)                 "
               "     Allroundders(AR  )             "
               "     Wicket-Keeper(WK)             ").pack()
Label(fm, text="").pack()

l1=Label(fm,text="Batsman (BAT)",font=('Comic Sans MS',9,"bold"))
l2=Label(fm,text="Bowers (BOW)",font=('Comic Sans MS',9,"bold"))
l3=Label(fm,text="Allroundders (AR)",font=('Comic Sans MS',9,"bold"))
l4=Label(fm,text="Wicket-Keeper (WK)",font=('Comic Sans MS',9,"bold"))
l1.place(x=3,y=23)
l2.place(x=140,y=23)
l3.place(x=275,y=23)
l4.place(x=420,y=23)

z1=StringVar()
z1.set("##")
z2=StringVar()
z2.set("##")
z3=StringVar()
z3.set("##")
z4=StringVar()
z4.set("##")

e1=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z1)
e1.place(x=97, y=26,width=15)
e2=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z2)
e2.place(x=230, y=26,width=15)
e3=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z3)
e3.place(x=386, y=26,width=15)
e4=Entry(fm,font=('arial',10,"italic"),bg="#F0F0F0",bd=0,fg='#399B9B',textvariable=z4)
e4.place(x=544, y=26,width=15)

e1.configure(state='disabled')
e2.configure(state='disabled')
e3.configure(state='disabled')
e4.configure(state='disabled')

zz1=StringVar()
zz1.initialize("####")
zz2=StringVar()
zz2.initialize("####")

Label(root,text="Point Available",bg="white",font=('Comic Sans MS',9,"bold")).place(x=120,y=120)
Label(root,text="Point Used",bg="white",font=('Comic Sans MS',9,"bold")).place(x=430,y=120)

e5=Entry(root,font=('arial',10,"italic","bold"), relief="solid",fg='#399B9B',textvariable=zz1)
e5.place(x=212, y=123,width=33)
e5.configure(state='disabled')
e6=Entry(root,font=('arial',10,"italic","bold"), relief="solid",fg='#399B9B',textvariable=zz2)
e6.place(x=500, y=123,width=33)
e6.configure(state='disabled')

b1 = Text(root, height=15, width=28, bg="white", relief="solid")
b1.place(x=80, y=150)
b1.configure(state='disabled')
b2 = Text(root, height=15, width=28, bg="white", relief="solid")
b2.place(x=380, y=150)
b2.configure(state='disabled')

selected = IntVar()
rad1 = Radiobutton(root, text='BAT', value=1, bg="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad2 = Radiobutton(root, text='BOW', value=2, bg="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad3 = Radiobutton(root, text='AR', value=3, bg="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad4 = Radiobutton(root, text='WK', value=4, bg="white", font=('Comic Sans MS',9), variable=selected,command=selection)
rad1.place(x=86, y=155)
rad2.place(x=144, y=155)
rad3.place(x=207, y=155)
rad4.place(x=256, y=155)
rad1.configure(state='disabled')
rad2.configure(state='disabled')
rad3.configure(state='disabled')
rad4.configure(state='disabled')
#rb = selected.get()
#print(rb)

Label(root,text=">",bg="white", font=('Comic Sans MS',20)).place(x=335,y=245)

Label(root,text="Team Name: ", bg="white", font=('Comic Sans MS',10)).place(x=405,y=155)

zzz=StringVar()
zzz.initialize("Displayed Here")
e7=Entry(root, font=('arial',10,"italic","bold"), relief="solid", fg='#399B9B', textvariable=zzz)
e7.place(x=485, y=157,width=100)
e7.configure(state='disabled')

'''
title2 = ['Programmer','Virat kohli', 'Developer','Yuvraj Singh', 'Designer']
titleList2 = Listbox(root, font=('Comic Sans MS',12), listvariable=title2, highlightcolor="white", bd=0, width=22, height=6, fg="#497CFF", selectbackground="#CCFFFF",selectforeground="#497CFF")
titleList2.focus_set()
for t in title2:
    titleList2.insert(END, t)
titleList2.place(x=385, y=200)
'''

#0
center(root)
root.mainloop()