import tkinter as tk
from tkinter import *

large_font = ('Verdana', 30)

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

    # Labels
    introLabel = Label(root, text="Hello!\n This is a simple CRC visualization!", bg="khaki3", fg="white",
                       font="none 24 bold")
    introLabel.config(anchor=CENTER)
    introLabel.pack()

    bitLabel = Label(root, text="Please enter the number of bits: ", bg="khaki3", fg="white", font="none 20 bold")
    bitLabel.place(relx=0.5, rely=0.2, anchor='center')

    pMessageLabel = Label(root, text="Please enter the P message: ", bg="khaki3", fg="white", font="none 20 bold")
    pMessageLabel.place(relx=0.5, rely=0.4, anchor='center')

    berLabel = Label(root, text="Please enter the Bit Error Rate(BER): ", bg="khaki3", fg="white", font="none 20 bold")
    berLabel.place(relx=0.5, rely=0.6, anchor='center')

    # Entry's

    bitEntry = Entry(root, font=("default", 15))
    bitEntry.place(relx=0.4, rely=0.25, width=200)

    pMessageEntry = Entry(root, font=("default", 15))
    pMessageEntry.place(relx=0.4, rely=0.45, width=200)

    berEntry = Entry(root, font=("default", 15))
    berEntry.place(relx=0.4, rely=0.65, width=200)

    root.mainloop()
