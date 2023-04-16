from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def guess_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def guess_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, width=280, fill="#000000", font=("Ariel", 20, "italic"),
                                                 text="Quiz Question")

        # Labels
        self.score_label = Label(text="Score: 0")
        self.score_label.config(fg="#FFFFFF", bg=THEME_COLOR)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(highlightbackground=THEME_COLOR, bg=THEME_COLOR, image=true_img,
                                  highlightthickness=0, command=self.guess_false)
        self.false_button = Button(highlightbackground=THEME_COLOR, bg=THEME_COLOR, image=false_img,
                                   highlightthickness=0, command=self.guess_true)

        # Grid Layout
        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
