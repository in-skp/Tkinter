# Grid Layout Demo - More
from Tkinter import *

root = Tk()

lblName = Label(root, text="Name")
lblPassword = Label(root, text="Password")
entryName = Entry(root)
entryPassword = Entry(root)

lblName.grid(row=0, column=0, sticky=E)
lblPassword.grid(row=1, column=0, sticky=E)

entryName.grid(row=0, column=1)
entryPassword.grid(row=1, column=1)

chkKeepLoggedIn = Checkbutton(root, text="Keep me logged in")
chkKeepLoggedIn.grid(columnspan=2)



root.mainloop()