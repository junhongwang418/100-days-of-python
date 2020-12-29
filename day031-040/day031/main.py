from tkinter import *
from tkmacosx import Button
import os
import sys
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_word = None
current_timer = None


def path(filepath: str):
    return os.path.join(sys.path[0], filepath)


def get_french_words():
    try:
        french_words = pandas.read_csv(path("data/words_to_learn.csv"))
    except:
        french_words = pandas.read_csv(path("data/french_words.csv"))

    return french_words.to_dict(orient="records")


def flip_card():
    global current_word
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(image, image=cardbackimage)


def next_card():
    global current_word, current_timer
    if current_timer is not None:
        window.after_cancel(current_timer)
    current_word = random.choice(french_words)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    canvas.itemconfig(image, image=cardfrontimage)
    current_timer = window.after(3000, flip_card)


def onclick_right():
    french_words.remove(current_word)

    with open(path("data/words_to_learn.csv"), 'w') as file:
        file.write(pandas.DataFrame(french_words).to_csv(index=False))

    next_card()


french_words = get_french_words()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

cardfrontimage = PhotoImage(file=path("images/card_front.gif"))
cardbackimage = PhotoImage(file=path("images/card_back.gif"))
rightimage = PhotoImage(file=path("images/right.gif"))
wrongimage = PhotoImage(file=path("images/wrong.gif"))

canvas = Canvas(width=cardfrontimage.width(), height=cardfrontimage.height(),
                bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(0, 0, image=cardfrontimage, anchor=NW)
title = canvas.create_text(cardfrontimage.width()/2,
                           cardfrontimage.height()/2 - 60,
                           text="French",
                           font=("Arial", 40, "italic"))
word = canvas.create_text(cardfrontimage.width()/2,
                          cardfrontimage.height()/2 + 60,
                          text="",
                          font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrongbutton = Button(width=wrongimage.width(), height=wrongimage.height(),
                     image=wrongimage, borderless=1, focusthickness=0, command=next_card)
wrongbutton.grid(row=1, column=0)

rightbutton = Button(width=rightimage.width(), height=rightimage.height(),
                     image=rightimage, borderless=1, focusthickness=0, command=onclick_right)
rightbutton.grid(row=1, column=1)

next_card()

window.mainloop()
