from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.total_guesses = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.update_scoreboard()

    def add_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def total_guesses(self):
        self.total_guesses += 1
