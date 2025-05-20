from turtle import Turtle

SHIP_COORDINATES = (0, -170)
MOVE_DISTANCE = 25

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("spaceship.gif")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(SHIP_COORDINATES)

    def move_left(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        self.forward(MOVE_DISTANCE)