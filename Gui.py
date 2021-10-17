import tkinter as tk
from tkinter import *

if __name__ == "__main__":
    # Window
    root = Tk()
    root.title("Gui")

    root.geometry("1000x1000")
    rootWidth = 1000
    rootHeight = 1000

    xLeft = int(root.winfo_screenwidth() / 2 - rootWidth / 2)
    yTop = int(root.winfo_screenheight() / 2 - rootHeight / 2)

    root.geometry("+{}+{}".format(xLeft, yTop))
    root.configure(bg="khaki3")

    # Label
    introLabel = Label(root, text="Hello!\n This is a simple CRC visualization", bg="khaki3", fg="white", font="none 24 bold")
    introLabel.config(anchor=CENTER)
    introLabel.pack()

    root.mainloop()
