from turtle import Turtle
from bullet import Bullet

SHIP_COORDINATES = (-200, -170)
MOVE_DISTANCE = 25

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("spaceship.gif")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(SHIP_COORDINATES)
        # Spaceship bullet list
        self.bullets = []

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        self.forward(MOVE_DISTANCE)