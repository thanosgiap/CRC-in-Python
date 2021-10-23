from tkinter import *
import CRC
import Utilities

large_font = ('Verdana', 30)
messagesToTransmit = 100000

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



    # Buttons

    def getinput():
        global finalMessage, alteredMessage
        errorMessages = 0
        foundError = 0

        bits = int(bitEntry.get())
        pMessage = [int(i) for i in str(pMessageEntry.get())]
        ber = float(berEntry.get())

        for i in range(messagesToTransmit):
            finalMessage = CRC.messageCreation(bits, pMessage)
            alteredMessage, errorMessages = CRC.messageWithNoise(finalMessage, ber, errorMessages)
            foundError = CRC.CRC_check(alteredMessage, pMessage, foundError)

        introLabel.destroy()
        bitLabel.destroy()
        pMessageLabel.destroy()
        berLabel.destroy()
        bitEntry.destroy()
        pMessageEntry.destroy()
        berEntry.destroy()
        calculateButton.destroy()

        # Output Labels
        messages = Label(root, text="Transmitted messages: " + str(Utilities.formatNumber(messagesToTransmit)),  bg="khaki3", fg="white", font="none 20 bold")
        messages.place(relx=0.5, rely=0.2, anchor='center')

        error = Label(root, text="Messages with errors: " + str(Utilities.formatNumber(errorMessages)) + " out of " + str(Utilities.formatNumber(messagesToTransmit)) + "("+
          str((errorMessages / messagesToTransmit) * 100) + "%)", bg="khaki3", fg="white", font="none 20 bold")
        error.place(relx=0.5, rely=0.3, anchor='center')

        found = Label(root, text="Messages with errors spotted by the CRC: " + str(Utilities.formatNumber(foundError)) + " out of " + str(Utilities.formatNumber(errorMessages)) + "(" + str((foundError / errorMessages) * 100) + "%)", bg="khaki3", fg="white", font="none 15 bold")
        found.place(relx=0.5, rely=0.4, anchor='center')

        notFound = Label(root, text="Messages with errors not spotted by the CRC: " + str(errorMessages - foundError) + " out of " + str(Utilities.formatNumber(errorMessages)) + "(" + str(((errorMessages - foundError) / errorMessages) * 100) + "%)", bg="khaki3", fg="white", font="none 15 bold")
        notFound.place(relx=0.5, rely=0.5, anchor='center')

    calculateButton = Button(root, text="Calculate", font=("default", 15), command=getinput)
    calculateButton.place(relx=0.4, rely=0.8, width=200)

    root.mainloop()
