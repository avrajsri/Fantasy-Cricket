import tkinter as tk


def demo(master):
    listbox = tk.Listbox(master)
    listbox.pack(expand=1, fill="both")

    # inserting some items
    listbox.insert("end", "A list item")

    for item in ["one", "two", "three", "four"]:
        listbox.insert("end", item)

    # this changes the background colour of the 2nd item
    listbox.itemconfig(1, {'bg':'red'})

    # this changes the font color of the 4th item
    listbox.itemconfig(3, {'fg': 'blue'})

    # another way to pass the colour
    listbox.itemconfig(2, bg='green')
    listbox.itemconfig(0, foreground="purple")


if __name__ == "__main__":
    root = tk.Tk()
    demo(root)
    root.mainloop()