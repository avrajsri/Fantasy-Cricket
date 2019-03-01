from tkinter import *


root = Tk()
root.title("Fantasy Cricket")
root.geometry("680x420")
root.resizable(width=FALSE,height=FALSE)

labelframe = LabelFrame(root, text="Your Selection")
labelframe.place(x=20,y=20)

left = Label(labelframe, text="")
left.pack()
left = Label(labelframe, text="     Batsman(BAT)           "
                              "     Bowers(BOW)             "
                              "     Allroundders(AR)           "
                              "     Wicket-Keeper(WK)               ")
left.pack()
left = Label(labelframe, text="")
left.pack()

root.mainloop()