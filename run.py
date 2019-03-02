from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("680x420")


b1 = Text(root, height=15, width=28, bg="white", relief="solid")
b1.place(x=80, y=150)
b1.configure(state='disabled')
b2 = Text(root, height=15, width=28, bg="white", relief="solid")
b2.place(x=380, y=150)
b2.configure(state='disabled')

selected = IntVar()
rad1 = Radiobutton(root, text='BAT', value=1, bg="white", font=('Comic Sans MS',9), variable=selected)
rad2 = Radiobutton(root, text='BOW', value=2, bg="white", font=('Comic Sans MS',9), variable=selected)
rad3 = Radiobutton(root, text='AR', value=3, bg="white", font=('Comic Sans MS',10), variable=selected)
rad4 = Radiobutton(root, text='WK', value=4, bg="white", font=('Comic Sans MS',10), variable=selected)
selected.set(1)
rad1.place(x=85, y=155)
rad2.place(x=137, y=155)
rad3.place(x=199, y=155)
rad4.place(x=253, y=155)

root.mainloop()