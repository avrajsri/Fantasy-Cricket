from tkinter import *


root=Tk()
root.title("Fantasy Cricket")
root.geometry("600x370")
root.resizable(width=FALSE,height=FALSE)
# -----------Show win in center--------------
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#0
center(root)
#1
variable = StringVar(root)
variable.set("Manage Teams") # default value
w = OptionMenu(root, variable, "NEW Team", "OPEN Team", "SAVE Team","EVALUATE Team")
w.place(x=0,y=0)

print(w)



root.mainloop()