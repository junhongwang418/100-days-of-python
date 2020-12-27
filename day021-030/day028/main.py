from tkinter import *
import os
import sys
from tkmacosx import Button

# # ---------------------------- GLOBAL ------------------------------- #
reps = 0
timer = None

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECOND_MS = 1000

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    titlelabel.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timertext, text="00:00")
    checklabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    if reps != 0:
        return

    restart_timer()


def restart_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        titlelabel.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        titlelabel.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        titlelabel.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Decrement count and call self every 1 second until count is 0"""
    global timer
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(SECOND_MS, count_down, count - 1)
    else:
        restart_timer()
        if reps % 2 == 0:
            checklabel.config(text=f"{checklabel.cget('text')}✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file=os.path.join(sys.path[0], "tomato.gif"))
canvas.create_image(100, 112, image=tomato_img)
timertext = canvas.create_text(100, 130, text="00:00", fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

titlelabel = Label(text="Timer", bg=YELLOW, fg=GREEN,
                   font=(FONT_NAME, 48, "normal"))
titlelabel.grid(row=0, column=1)

startbutton = Button(text="Start", borderless=1, command=start_timer)
startbutton.grid(row=2, column=0)

resetbutton = Button(text="Reset", borderless=1, command=reset_timer)
resetbutton.grid(row=2, column=2)

checklabel = Label(text="", bg=YELLOW, fg=GREEN)
checklabel.grid(row=3, column=1)

window.mainloop()
