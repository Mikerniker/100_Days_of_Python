from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Text goes here",
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        
        self.score = Label(text="Score: 0",
                           font=("Arial", 10),
                           bg=THEME_COLOR,
                           fg="WHITE")
        self.score.grid(row=0, column=1)
        self.score.config(padx=20, pady=20)


        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_img, highlightthickness=0, command=self.check_true)
        self.correct_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)