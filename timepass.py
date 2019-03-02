from tkinter import *
root = Tk()
root.configure(bg="#FFFFFF")
root.geometry("680x420")

title = ["","",'Programmer','Virat kohli', 'Developer','Yuvraj Singh', 'Web Developer', 'Designer']

titleList = Listbox(root, listvariable=title, bd=0, height=8, fg="#497CFF", font=('Comic Sans MS',10), selectbackground="#CCFFFF",selectforeground="#497CFF")
for t in title:
	titleList.insert(END, t)
titleList.place(x=10, y=10)

selected = IntVar()
rad1 = Radiobutton(root, text='BAT', value=1,bg="white", font=('Comic Sans MS',9), variable=selected)
rad2 = Radiobutton(root, text='BOW', value=2,bg="white", font=('Comic Sans MS',9), variable=selected)
rad3 = Radiobutton(root, text='AR', value=3,bg="white", font=('Comic Sans MS',10), variable=selected)
rad4 = Radiobutton(root, text='WK', value=4,bg="white", font=('Comic Sans MS',10), variable=selected)
selected.set(1)
rad1.place(x=180, y=30)
rad2.place(x=240, y=30)
rad3.place(x=300, y=30)
rad4.place(x=350, y=30)


root.mainloop()