from turtle import Turtle
from bullet import Bullet

SHIP_COORDINATES = (-200, -170)
MOVE_DISTANCE = 30

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
        if self.xcor() > -220:
            self.backward(MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < 220:
            self.forward(MOVE_DISTANCE)

    def create_bullet(self):
        new_bullet = Bullet()
        new_bullet.position_bullet(self.pos())
        self.bullets.append(new_bullet)

    def reset_position(self):
        self.goto(SHIP_COORDINATES)
