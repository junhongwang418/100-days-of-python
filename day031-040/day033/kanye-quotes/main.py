from tkinter import *
from tkmacosx import Button
import requests
import sys
import os


def get_quote():
    res = requests.get("https://api.kanye.rest/")
    res.raise_for_status()
    data = res.json()
    quote = data.get("quote")
    canvas.itemconfig(quote_text, text=quote)


def path(relative_filepath):
    return os.path.join(sys.path[0], relative_filepath)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=path("background.gif"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
    "Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=path("kanye.gif"))
kanye_button = Button(image=kanye_img, borderless=1,
                      highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
