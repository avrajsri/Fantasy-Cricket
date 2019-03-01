from tkinter import *

COLOR1 = "black"
COLOR2 = "blue"

root = Tk()
root.config(bg=COLOR1)

button = Button(text="button", bg=COLOR2)
button.pack(padx=5, pady=5)

root.mainloop()