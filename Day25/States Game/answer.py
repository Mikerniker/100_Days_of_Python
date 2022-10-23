from turtle import Turtle


class Answer(Turtle):
    def __init__(self):
        super().__init__()

    def write_map(self, answer, x, y):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(answer, align="left", font=("Courier", 8, "normal"))