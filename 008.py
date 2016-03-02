from Tkinter import *

class SantoButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack()

    def printMessage(self):
        print("Wow Its working")


root = Tk()
b = SantoButtons(root)
root.mainloop()