from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(position)
        # self.goto(0, -250)


    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())