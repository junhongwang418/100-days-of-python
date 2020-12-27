import random
from tkinter import *
from tkinter import messagebox
import os
import sys
from tkmacosx import Button
import pyperclip

FILE_NAME = 'data.txt'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    passwordentry.delete(0, END)
    passwordentry.insert(END, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    if websiteentry.get() == "" or passwordentry.get() == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any field empty!")
        return

    ok = messagebox.askokcancel(title=websiteentry.get(), message=f"These are the details entered: \n"
                                f"Email: {emailusernameentry.get()}\n"
                                f"Password: {passwordentry.get()}\n"
                                f"Is it ok to save?")

    if not ok:
        return

    with open(os.path.join(sys.path[0], FILE_NAME), 'a') as data:
        data.write(
            f"{websiteentry.get()} | {emailusernameentry.get()} | {passwordentry.get()}\n")

    websiteentry.delete(0, END)
    passwordentry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=os.path.join(sys.path[0], "logo.gif"))
canvas.create_image(0, 0, image=logo_img, anchor=NW)
canvas.grid(row=0, column=0, columnspan=3)

websitelabel = Label(text="Website:")
websitelabel.grid(row=1, column=0)

emailusernamelabel = Label(text="Email/Username:")
emailusernamelabel.grid(row=2, column=0)

passwordlabel = Label(text="Password")
passwordlabel.grid(row=3, column=0)

websiteentry = Entry()
websiteentry.focus()
websiteentry.grid(row=1, column=1, columnspan=2, sticky=NSEW)

emailusernameentry = Entry()
emailusernameentry.insert(END, "junhong@gmail.com")
emailusernameentry.grid(row=2, column=1, columnspan=2, sticky=NSEW)

passwordentry = Entry()
passwordentry.grid(row=3, column=1, sticky=NSEW)

generatepasswordbutton = Button(
    text="Generate Password", borderless=1, command=generate_password)
generatepasswordbutton.grid(row=3, column=2, sticky=NSEW)

addbutton = Button(text="Add", borderless=1, command=save)
addbutton.grid(row=4, column=1, columnspan=2, sticky=NSEW)


window.mainloop()
