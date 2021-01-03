
from tkinter import *
from tkmacosx import Button
import os
import sys
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


def path(filepath):
    return os.path.join(sys.path[0], filepath)


class QuizInterface:

    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scorelabel = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scorelabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(150, 125, text="", width=280,
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        falseimage = PhotoImage(file=path("images/false.gif"))
        self.falsebutton = Button(image=falseimage, width=100, height=97, borderless=1,
                                  highlightthickness=0, command=self.onclick_falsebutton)
        self.falsebutton.grid(row=2, column=0)

        trueimage = PhotoImage(file=path("images/true.gif"))
        self.truebutton = Button(image=trueimage, width=100, height=97, borderless=1,
                                 highlightthickness=0, command=self.onclick_truebutton)
        self.truebutton.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def onclick_falsebutton(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def onclick_truebutton(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")
