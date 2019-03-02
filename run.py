from tkinter import *
root = Tk()
root.geometry("680x420")

title = ['    Programmer', '    Developer', '   Web Developer', '    Designer']

titleList = Listbox(root, height=5, fg="#399B9B", font=('Comic Sans MS',9))
for t in title:
	titleList.insert(END, t)
titleList.place(x=60, y=60)


root.mainloop()

