from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Fantasy Cricket")
root.geometry("680x490")
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

#5
def go(event):#==========================================================================================================================

    j=lt1.curselection()
    jj=j[0]

    c.execute("SELECT * FROM DATA")
    data = c.fetchall()
    TotalP=[]
    for i in data:
        TotalP.append(i)

    global ee1
    global ee2
    global ee3
    global ee4
    global ee5
    global ee6
    global ee7
    global pp1

    if(sn==1):
        u = batP[jj]
        ee1=ee1+1
        for i in TotalP:
            if i[0] == u:
                ee6=i[2]

        if(int(ee1)<int(5)):
            pp1=pp1+ee6
            e6.configure(text=pp1)
            e1.configure(text=ee1)
            lt2.insert(END,u)
            batP.remove(u)
            lt1.delete(j)

        else:
            messagebox.showwarning("Team Formation", "Cannot Select More Than 4 Batsmen !")

    elif(sn==2):
        u = bowP[jj]
        ee2=ee2+1
        for i in TotalP:
            if i[0] == u:
                ee6=i[2]

        if (int(ee2) < int(4)):
            pp1=pp1+ee6
            e6.configure(text=pp1)
            e2.configure(text=ee2)
            lt2.insert(END,u)
            bowP.remove(u)
            lt1.delete(j)

        else:
            messagebox.showwarning("Team Formation", "Cannot Select More Than 3 Bowlers !")

    elif(sn==3):
        u = arP[jj]
        ee3=ee3+1
        for i in TotalP:
            if i[0] == u:
                ee6=i[2]

        if (int(ee3) < int(4)):
            pp1=pp1+ee6
            e6.configure(text=pp1)
            e3.configure(text=ee3)
            arP.remove(u)
            lt2.insert(END,u)
            lt1.delete(j)

        else:
            messagebox.showwarning("Team Formation", "Cannot Select More Than 3 Allrounders !")

    else:
        u = wkP[jj]
        ee4=ee4+1
        for i in TotalP:
            if i[0] == u:
                ee6=i[2]

        if (int(ee4) < int(2)):
            pp1=pp1+ee6
            e6.configure(text=pp1)
            e4.configure(text=ee4)
            wkP.remove(u)
            lt2.insert(END,u)
            lt1.delete(j)

        else:
            messagebox.showwarning("Team Formation", "Cannot Select More Than 1 Allrounders !")

    v=1000-int(pp1)
    if(int(v)<1001 and int(v)>-1):
        e5.configure(text=v)

    else:
        messagebox.showerror("Error", "Insufficient Points Available !\nYou Can not Buy This Player !")
        NEW()

#4
def selection():#==========================================================================================================================

    global sn
    sn = selected.get()
    lt1.delete(0, END)

    if(sn==1):
        for i in batP:
            lt1.insert(END, i)

    elif(sn==2):
        for i in bowP:
            lt1.insert(END, i)

    elif(sn==3):
        for i in arP:
            lt1.insert(END, i)

    else:
        for i in wkP:
            lt1.insert(END, i)

#3
def GV():#==========================================================================================================================

    global conn
    global c
    conn = sqlite3.connect('Cricket.db')
    c = conn.cursor()

    global TotalP
    global batP
    global bowP
    global arP
    global wkP
    global ee1
    global ee2
    global ee3
    global ee4
    global ee5
    global ee6
    global ee7
    global pp1
    TotalP=[]
    batP=[]
    bowP=[]
    arP=[]
    wkP=[]
    ee1=0
    ee2=0
    ee3=0
    ee4=0
    ee5=0
    ee6=1000
    ee7=0
    pp1=0

    c.execute("SELECT * FROM DATA")
    data = c.fetchall()
    for i in data:
        TotalP.append(i)

    lt1.delete(0, END)

    for i in TotalP:
        if i[1]=="BAT":
            batP.append(i[0])


    for i in TotalP:
        if i[1]=="BOW":
            bowP.append(i[0])


    for i in TotalP:
        if i[1]=="AR":
            arP.append(i[0])


    for i in TotalP:
        if i[1]=="WK":
            wkP.append(i[0])

#2
def NEW():#==========================================================================================================================

    GV()
    lt1.delete(0, END)
    lt2.delete(0, END)

    def tname():
        global tn
        tn=en.get().upper()

        try:
            global conn
            global c
            conn = sqlite3.connect('Cricket.db')
            c = conn.cursor()

            c.execute("CREATE TABLE " + tn + "(player TEXT, Tin INTEGER, ctg TEXT)")
            conn.commit()
            c.execute("DROP TABLE "+tn+"")
            conn.commit()
            root1.destroy()

            e1.configure(text=0)
            e2.configure(text=0)
            e3.configure(text=0)
            e4.configure(text=0)
            e5.configure(text=1000)
            e6.configure(text=0)
            e7.configure(text="\"" + tn + "\"")

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
            lt1.delete(0, END)
            lt2.delete(0, END)

            root1.destroy()

            messagebox.showwarning("Value Error", "Enter Valid Team Name !")

    def q():
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
            lt1.delete(0, END)
            lt2.delete(0, END)

            root1.destroy()

    root1 = Tk()
    root1.title("New Team")
    root1.geometry("380x200")
    root1.resizable(width=FALSE, height=FALSE)

    Label(root1, text="Enter Team Name: ", font=('Comic Sans MS', 12)).place(x=30, y=40)
    en = Entry(root1, font=('arial', 12, "bold"), bg="#F0F0F0", bd=5, highlightthickness=2, highlightcolor="black")
    en.focus_set()
    en.place(x=180, y=40, width=150)

    b1=Button(root1, text="OK", font=('Comic Sans MS', 10), relief=RAISED, bd=3, width=10, command=tname)
    b1.place(x=80, y=110)
    b2=Button(root1, text="Exit", font=('Comic Sans MS', 10), relief=RAISED, bd=3, width=10, command=q)
    b2.place(x=220, y=110)

    center(root1)
    root1.mainloop()

#6
def OPEN():#==========================================================================================================================

    def f2(z):
        lt3.delete(0, END)
        c.execute("SELECT * FROM TeamData WHERE TeamName = ?", [z])
        data = c.fetchall()
        data = data[0]
        p = list(data)
        p.remove(z)

        for i in p:
            lt3.insert(END, i)

    def f1(event):
        global x
        x = variable.get()
        xx = x[0]
        f2(xx)

    root2 = Tk()
    root2.title("OPEN Team")
    root2.geometry("400x390")
    root2.resizable(width=FALSE, height=FALSE)
    center(root2)

    b2 = Text(root2, height=4, width=40, bg="#F0F0F0", relief="solid")
    b2.place(x=40, y=20)
    b2.configure(state='disabled')

    Label(root2, text="Select Team Name :", font=('arial', 14, "italic"), bg="#F0F0F0", bd=0, fg='#399B9B').place(x=60,
                                                                                                                  y=43)

    Pname = []
    conn = sqlite3.connect('Cricket.db')
    c = conn.cursor()
    c.execute("SELECT TeamName FROM TeamData")
    data = c.fetchall()
    for i in data:
        Pname.append(i)

    variable = Variable(root2)
    variable.set("\"" + "Click Me" + "\"")

    w = OptionMenu(root2, variable, *Pname, command=f1)
    w.place(x=250, y=40)

    b3 = Text(root2, height=16.5, width=28, bg="white", relief="solid")
    b3.place(x=90, y=100)
    b3.configure(state='disabled')

    lt3 = Listbox(root2, font=('Comic Sans MS', 12), highlightcolor="white", bd=0, width=22, height=11,
                  fg="#497CFF", selectbackground="#CCFFFF", selectforeground="#497CFF")
    lt3.place(x=93, y=103)

#7
def SAVE():#==========================================================================================================================

    try:
        global conn
        global c
        conn = sqlite3.connect('Cricket.db')
        c = conn.cursor()

        x=lt2.get(0,END)



        if(len(x)==11):
            c.execute("INSERT INTO TeamData(TeamName, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (tn, x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10]))
            conn.commit()
            messagebox.showinfo("Team Created", "Best Of Luck.")

        else:
            messagebox.showerror("Error", "11 Player Required For Cricket Match !")


    except Exception as e:
        messagebox.showwarning("Error", str(e))


    NEW()

#8
def EVALUATE():#==========================================================================================================================

    def f4(cc):
        global POINT
        POINT = 0

        runsscored = cc[1]
        ballsfaced = cc[2]
        fours = cc[3]
        sixes = cc[4]
        bowled = cc[5]
        runsgiven = cc[6]
        wickets = cc[7]
        catches = cc[8]
        stumpings = cc[9]
        runouts = cc[10]

        ## BATTING POINT-------------------------------------------------------

        # 1 point for 2 runs scored
        POINT += runsscored // 2
        # Additional 5 points for half century
        if runsscored >= 50:
            POINT += 5
        # Additional 10 points for century
        if runsscored >= 100:
            POINT += 10
        if ballsfaced > 0:
            # strike_rate = runs/balls_faced
            strike_rate = (runsscored / ballsfaced) * 100
            # 4 points for strike rate>100
            if strike_rate > 100:
                POINT += 4
            # 2 points for strike rate of 80-100
            elif strike_rate >= 80:
                POINT += 2
        # 1 point for hitting a boundary (four)
        POINT += fours
        # 2 points for over boundary(six)
        POINT += 2 * sixes

        ## BOLWLNG POINT-------------------------------------------------------

        # 10 points for each wicket
        POINT += (10 * wickets)
        # Additional 5 points for three wickets per innings
        if wickets >= 3:
            POINT += 5
        # Additional 10 points for 5 wickets or more in innings
        if wickets >= 5:
            POINT += 10
        if bowled > 0:
            economy_rate = (runsgiven / bowled) * 6
            # 4 points for economy rate between 3.5 and 4.5
            if (economy_rate >= 3.5 and economy_rate <= 4.5):
                POINT += 4
            # 7 points for economy rate between 2 and 3.5
            elif (economy_rate >= 2 and economy_rate < 3.5):
                POINT += 7
            # 10 points for economy rate less than 2
            elif (economy_rate < 2):
                POINT += 10

        ## FIELDING POINT-------------------------------------------------------
        # 10 points each for catch/stumping/run out
        POINT += 10 * (catches + stumpings + runouts)

        xx = lt5.get(0, END)
        xx = len(xx)
        if (11 > xx):
            lt5.insert(END, POINT)

        else:
            pass

    def f3():
        v1 = variable1.get()
        v1 = v1[0]
        v2 = variable2.get()

        global conn
        global c
        conn = sqlite3.connect('Cricket.db')
        c = conn.cursor()

        c.execute("SELECT * from TeamData WHERE TeamName = ?", (v1,))
        tp = c.fetchone()
        tp = tp[1:]

        for td in tp:
            c.execute("SELECT * from " + v2 + " WHERE name = ?", (td,))
            cc = c.fetchone()
            f4(cc)

        t = 0
        g = lt5.get(0, END)
        for i in g:
            t += i
        e8.configure(text=t)

    def f2(event):
        e8.configure(text="####")
        lt5.delete(0, END)

        k = variable1.get()
        if (k == "\"Select Team\""):
            b.configure(state=DISABLED)

        else:
            b.configure(state=NORMAL)

    def f1(event):
        e8.configure(text="####")
        x = variable1.get()
        global z
        global k
        z = x[0]
        k = variable2.get()
        lt4.delete(0, END)
        lt5.delete(0, END)
        c.execute("SELECT * FROM TeamData WHERE TeamName = ?", [z])
        data = c.fetchall()
        data = data[0]
        p = list(data)
        p.remove(z)

        for i in p:
            lt4.insert(END, i)

        if (k == "\"Select Match\""):
            b.configure(state=DISABLED)

        else:
            b.configure(state=NORMAL)

    root3 = Tk()
    root3.title("EVALUATE Team")
    root3.geometry("500x450")
    root3.resizable(width=FALSE, height=FALSE)
    center(root3)

    b2 = Text(root3, height=4, width=57, bg="#F0F0F0", relief="solid")
    b2.place(x=20, y=10)
    b2.configure(state='disabled')

    Label(root3, text="Evaluate the Performance of your Fantasy Team", font=('arial', 12, "italic", "bold"),
          bg="#F0F0F0", bd=0, fg='#399B9B').place(x=65, y=15)

    Pname = []
    conn = sqlite3.connect('Cricket.db')
    c = conn.cursor()
    c.execute("SELECT TeamName FROM TeamData")
    data = c.fetchall()
    for i in data:
        Pname.append(i)

    variable1 = Variable(root3)
    variable1.set("\"" + "Select Team" + "\"")
    w1 = OptionMenu(root3, variable1, *Pname, command=f1)
    w1.place(x=80, y=40, width=120)

    Game = ["Match1", "Match2", "Match3", "Match4", "Match5"]
    variable2 = Variable(root3)
    variable2.set("\"" + "Select Match" + "\"")
    w2 = OptionMenu(root3, variable2, *Game, command=f2)
    w2.place(x=300, y=40, width=120)

    b4 = Text(root3, height=17, width=25, bg="white", relief="solid")
    b4.place(x=30, y=100)
    b4.configure(state='disabled')

    b5 = Text(root3, height=17, width=25, bg="white", relief="solid")
    b5.place(x=270, y=101)
    b5.configure(state='disabled')

    lt4 = Listbox(root3, font=('Comic Sans MS', 12), highlightcolor="white", bd=0, width=20, height=11,
                  fg="#497CFF", selectbackground="#CCFFFF", selectforeground="#497CFF")
    lt4.place(x=31, y=101)

    lt5 = Listbox(root3, font=('Comic Sans MS', 12), highlightcolor="white", bd=0, width=20, height=11,
                  fg="#497CFF", selectbackground="#CCFFFF", selectforeground="#497CFF")
    lt5.place(x=271, y=102)

    Label(root3, text="Total Points: ", font=('arial', 13, "bold"), bg="#F0F0F0", bd=0).place(x=55, y=400)

    e8 = Label(root3, text="####", font=('arial', 13, "italic", "bold"), fg='#399B9B')
    e8.place(x=155, y=399)

    b = Button(root3, text="Calculate Score", bd=3, command=f3, state=DISABLED)
    b.place(x=320, y=398)

    Pname = []
    conn = sqlite3.connect('Cricket.db')
    c = conn.cursor()
    c.execute("SELECT TeamName FROM TeamData")
    data = c.fetchall()
    for i in data:
        Pname.append(i)


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

b1 = Text(root, height=20, width=28, bg="white", relief="solid")
b1.place(x=80, y=150)
b1.configure(state='disabled')
b2 = Text(root, height=20, width=28, bg="white", relief="solid")
b2.place(x=380, y=150)
b2.configure(state='disabled')

Label(root,text=">",bg="white", font=('Comic Sans MS',20)).place(x=335,y=245)
Label(root,text="Team Name: ", bg="white", font=('Comic Sans MS',10)).place(x=405,y=155)
e7=Label(root,text="Displayed Here", font=('arial',10,"bold"),bg="white", fg='#399B9B', anchor="w")
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

lt1 = Listbox(root, font=('Comic Sans MS', 12), highlightcolor="white", bd=0, width=22, height=11,
                     fg="#497CFF", selectbackground="#CCFFFF", selectforeground="#497CFF")
lt1.bind("<Double-1>", go)
lt1.place(x=83, y=199)


lt2 = Listbox(root, font=('Comic Sans MS',12), highlightcolor="white", bd=0, width=22, height=11,
              fg="#497CFF", selectbackground="#CCFFFF",selectforeground="#497CFF")
lt2.place(x=385, y=199)

GV()

#0
center(root)
root.mainloop()