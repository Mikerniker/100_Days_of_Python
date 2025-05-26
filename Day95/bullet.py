from turtle import Turtle

MOVE_DISTANCE = 30

class Bullet(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()
      self.shapesize(stretch_len=0.2, stretch_wid=0.2)
      self.color("white")
      self.speed(10)

    def create_bullet(self, position):
       self.goto(position)


    def move_bullet(self):
       self.forward(MOVE_DISTANCE)