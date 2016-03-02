# Grid Layout Demo
from Tkinter import *

root = Tk()

lblName = Label(root, text="Name")
lblPassword = Label(root, text="Password")
entryName = Entry(root)
entryPassword = Entry(root)

lblName.grid(row=0, column=0)
lblPassword.grid(row=1, column=0)

entryName.grid(row=0, column=1)
entryPassword.grid(row=1, column=1)



root.mainloop()