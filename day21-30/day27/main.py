from tkinter import *
from tkmacosx import Button

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

inputmiles = Entry(width=10)
inputmiles.insert(END, string="0")
inputmiles.grid(row=0, column=1)

labelmiles = Label(text="Miles")
labelmiles.grid(row=0, column=2)

labelisequalto = Label(text="is equal to")
labelisequalto.grid(row=1, column=0)

labelres = Label(text="0")
labelres.grid(row=1, column=1)

labelkm = Label(text="Km")
labelkm.grid(row=1, column=2)


def oncalculate():
    miles = int(inputmiles.get())
    labelres.config(text=str(round(miles/0.62137)))


buttoncalculate = Button(
    text="Calculate", borderless=1, fg='black', bg='white', command=oncalculate)
buttoncalculate.grid(row=2, column=1)


window.mainloop()
