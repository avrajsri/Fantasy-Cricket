from tkinter import *
root = Tk()
root.geometry("680x420")

title = ['    Programmer','    Virat kohli', '    Developer','    Yuvraj Singh', '    Web Developer', '    Designer']

titleList = Listbox(root, bd=0, height=8, fg="#497CFF", font=('Comic Sans MS',10), selectbackground="#CCFFFF",selectforeground="#497CFF")
titleList.focus_set()
for t in title:
	titleList.insert(END, t)
titleList.place(x=10, y=10)

root.mainloop()