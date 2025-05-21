from turtle import Turtle

MOVE_DISTANCE = 20


class Bullet(Turtle):
   def __init__(self):
       super().__init__()
       self.shape("circle")
       self.setheading(90)
       self.penup()
       self.shapesize(stretch_len=0.5, stretch_wid=0.5)
       self.color("white")