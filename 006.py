from Tkinter import *

root = Tk()

def printName():
    print("Hello my name is Snatosh!")

btnPrintName = Button(root, text="Print Name", command=printName)
btnPrintName.pack()

root.mainloop()